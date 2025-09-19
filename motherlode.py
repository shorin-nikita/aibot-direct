#!/usr/bin/env python3
"""
motherlode.py

Interactive setup script for the Local AI Package.
Greets from SHORIN and guides the user through configuration.
"""

import os
import secrets
import subprocess
import sys
from pathlib import Path

def generate_random_key(length=32):
    """Generate a random hex key of specified length."""
    return secrets.token_hex(length)

def print_shorin_greeting():
    """Print the greeting from SHORIN."""
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                    Welcome to Motherlode!                    ║
║                                                              ║
║                Greetings from SHORIN!                        ║
║                                                              ║
║   This script will guide you through setting up your        ║
║   Local AI Package with n8n and Supabase.                    ║
║                                                              ║
║   Let's get your AI infrastructure up and running!          ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
""")

def get_user_input():
    """Get user input for configuration."""
    print("\n📋 Configuration Setup")
    print("=" * 50)

    # Get hostnames
    n8n_hostname = input("N8N_HOSTNAME (e.g., n8n.yourdomain.com): ").strip()
    supabase_hostname = input("SUPABASE_HOSTNAME (e.g., supabase.yourdomain.com): ").strip()
    letsencrypt_email = input("LETSENCRYPT_EMAIL (your email for SSL certificates): ").strip()

    # Get secrets
    jwt_secret = input("JWT_SECRET (your super secret JWT token, at least 32 chars): ").strip()
    anon_key = input("ANON_KEY (Supabase anonymous key): ").strip()
    service_role_key = input("SERVICE_ROLE_KEY (Supabase service role key): ").strip()

    return {
        'n8n_hostname': n8n_hostname,
        'supabase_hostname': supabase_hostname,
        'letsencrypt_email': letsencrypt_email,
        'jwt_secret': jwt_secret,
        'anon_key': anon_key,
        'service_role_key': service_role_key
    }

def generate_passwords():
    """Generate random passwords and keys."""
    print("\n🔐 Generating secure passwords and keys...")

    return {
        'n8n_encryption_key': generate_random_key(32),
        'n8n_user_management_jwt_secret': generate_random_key(32),
        'postgres_password': generate_random_key(16),
        'dashboard_password': generate_random_key(16),
        'pooler_tenant_id': '1000'
    }

def update_env_file(user_config, generated_config):
    """Update the .env file with user and generated configuration."""
    env_path = Path('.env')
    env_example_path = Path('.env.example')

    if not env_path.exists():
        if env_example_path.exists():
            print("📋 Creating .env file from .env.example...")
            import shutil
            shutil.copyfile(env_example_path, env_path)
        else:
            print("❌ Neither .env nor .env.example file found! Please ensure you're in the correct directory.")
            sys.exit(1)

    print("\n📝 Updating .env file...")

    # Read current .env content
    with open(env_path, 'r') as f:
        content = f.read()

    # Replace values
    replacements = {
        'N8N_ENCRYPTION_KEY=super-secret-key': f'N8N_ENCRYPTION_KEY={generated_config["n8n_encryption_key"]}',
        'N8N_USER_MANAGEMENT_JWT_SECRET=even-more-secret': f'N8N_USER_MANAGEMENT_JWT_SECRET={generated_config["n8n_user_management_jwt_secret"]}',
        'POSTGRES_PASSWORD=your-super-secret-and-long-postgres-password': f'POSTGRES_PASSWORD={generated_config["postgres_password"]}',
        'JWT_SECRET=your-super-secret-jwt-token-with-at-least-32-characters-long': f'JWT_SECRET={user_config["jwt_secret"]}',
        'ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyAgCiAgICAicm9sZSI6ICJhbm9uIiwKICAgICJpc3MiOiAic3VwYWJhc2UtZGVtbyIsCiAgICAiaWF0IjogMTY0MTc2OTIwMCwKICAgICJleHAiOiAxNzk5NTM1NjAwCn0.dc_X5iR_VP_qT0zsiyj_I_OZ2T9FtRU2BBNWN8Bu4GE': f'ANON_KEY={user_config["anon_key"]}',
        'SERVICE_ROLE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyAgCiAgICAicm9sZSI6ICJzZXJ2aWNlX3JvbGUiLAogICAgImlzcyI6ICJzdXBhYmFzZS1kZW1vIiwKICAgICJpYXQiOiAxNjQxNzY5MjAwLAogICAgImV4cCI6IDE3OTk1MzU2MDAKfQ.DaYlNEoUrrEn2Ig7tqibS-PHK5vgusbcbo7X36XVt4Q': f'SERVICE_ROLE_KEY={user_config["service_role_key"]}',
        'DASHBOARD_PASSWORD=this_password_is_insecure_and_should_be_updated': f'DASHBOARD_PASSWORD={generated_config["dashboard_password"]}',
        'POOLER_TENANT_ID=your-tenant-id': f'POOLER_TENANT_ID={generated_config["pooler_tenant_id"]}',
        '# N8N_HOSTNAME=n8n.yourdomain.com': f'N8N_HOSTNAME={user_config["n8n_hostname"]}',
        '# SUPABASE_HOSTNAME=supabase.yourdomain.com': f'SUPABASE_HOSTNAME={user_config["supabase_hostname"]}',
        '# LETSENCRYPT_EMAIL=internal': f'LETSENCRYPT_EMAIL={user_config["letsencrypt_email"]}',
        'CLICKHOUSE_PASSWORD=super-secret-key-1': f'CLICKHOUSE_PASSWORD={generate_random_key(16)}',
        'MINIO_ROOT_PASSWORD=super-secret-key-2': f'MINIO_ROOT_PASSWORD={generate_random_key(16)}',
        'LANGFUSE_SALT=super-secret-key-3': f'LANGFUSE_SALT={generate_random_key(16)}',
        'NEXTAUTH_SECRET=super-secret-key-4': f'NEXTAUTH_SECRET={generate_random_key(32)}',
        'ENCRYPTION_KEY=generate-with-openssl # generate via `openssl rand -hex 32`': f'ENCRYPTION_KEY={generate_random_key(32)}',
        'FLOWISE_USERNAME=': f'FLOWISE_USERNAME=admin',
        'FLOWISE_PASSWORD=': f'FLOWISE_PASSWORD={generate_random_key(12)}'
    }

    for old, new in replacements.items():
        content = content.replace(old, new)

    # Write back to file
    with open(env_path, 'w') as f:
        f.write(content)

    print("✅ .env file updated successfully!")

def check_docker_availability():
    """Check if Docker is available on the system."""
    try:
        result = subprocess.run(['docker', '--version'],
                              capture_output=True, text=True, check=True)
        print("✅ Docker is available")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Docker is not installed or not available")
        print()
        print("📦 Please install Docker first:")
        print()
        print("🐧 Ubuntu/Debian:")
        print("   sudo apt update && sudo apt install docker.io docker-compose")
        print()
        print("🍎 macOS:")
        print("   Download Docker Desktop from: https://www.docker.com/products/docker-desktop")
        print()
        print("🔥 After installing Docker, also set up firewall (if needed):")
        print("   sudo ufw enable")
        print("   sudo ufw allow 80 && sudo ufw allow 443")
        print("   sudo ufw reload")
        print()
        return False

def run_start_services(user_config):
    """Run the start_services.py script."""
    print("\n🚀 Starting services...")

    # Check Docker availability first
    if not check_docker_availability():
        print("\n💡 Configuration saved! Run this script again after installing Docker.")
        print(f"Access URLs after setup: https://{user_config['n8n_hostname']} and https://{user_config['supabase_hostname']}")
        return

    try:
        # Run start_services.py with default parameters
        result = subprocess.run([
            sys.executable, 'start_services.py',
            '--profile', 'cpu',
            '--environment', 'private'
        ], check=True)

        print("✅ Services started successfully!")
        print("\n🎉 Setup complete!")
        print("Your Local AI Package is now running.")
        print(f"Access n8n at: https://{user_config['n8n_hostname']}")
        print(f"Access Supabase at: https://{user_config['supabase_hostname']}")

    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to start services: {e}")
        print("\n🔧 Troubleshooting:")
        print("- Make sure Docker is running")
        print("- Check if ports 80 and 443 are available")
        print("- Try running: python3 start_services.py --profile cpu --environment private")
        sys.exit(1)

def check_directory():
    """Check if we're in the correct directory."""
    required_files = ['.env.example', 'docker-compose.yml', 'start_services.py']
    missing_files = []

    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)

    if missing_files:
        print("❌ Error: This script must be run from the local-ai-packaged directory!")
        print(f"Missing required files: {', '.join(missing_files)}")
        print(f"Current directory: {Path.cwd()}")
        print()
        print("Please navigate to the correct directory:")
        print("  cd local-ai-packaged")
        print("  python3 motherlode.py")
        sys.exit(1)

    print("✅ Running from correct directory: local-ai-packaged")

def main():
    """Main function."""
    print_shorin_greeting()

    # Check if we're in the right directory
    check_directory()

    # Get user configuration
    user_config = get_user_input()

    # Generate passwords
    generated_config = generate_passwords()

    # Update .env file
    update_env_file(user_config, generated_config)

    # Run start services
    run_start_services(user_config)

if __name__ == "__main__":
    main()
