#!/usr/bin/env python3
"""AIBot Direct Test Launcher"""
import sys
import secrets
import string

class AIBotDirectLauncher:
    def __init__(self):
        self.version = "1.0.0"
        self.website = "https://AIBot.Direct"
    
    def print_banner(self):
        print("🤖 AIBot Direct - AI Automation Platform")
        print(f"🌐 Website: {self.website}")
        print("🏗️ Based on local-ai-packaged by Cole Medin")
    
    def generate_env_file(self):
        alphabet = string.ascii_letters + string.digits
        n8n_key = ''.join(secrets.choice(alphabet) for _ in range(32))
        postgres_pass = ''.join(secrets.choice(alphabet) for _ in range(24))
        
        env_content = f"""# AIBot Direct Test Configuration
N8N_ENCRYPTION_KEY={n8n_key}
POSTGRES_PASSWORD={postgres_pass}
POOLER_TENANT_ID=aibot-direct-{secrets.randbelow(10000):04d}
"""
        with open(".env", "w") as f:
            f.write(env_content)
        return True

def main():
    if "--help" in sys.argv:
        print("Usage: python3 aibot_start.py [--profile cpu|gpu-nvidia]")
        return
    
    launcher = AIBotDirectLauncher()
    launcher.print_banner()
    launcher.generate_env_file()
    print("✅ Test version ready!")

if __name__ == "__main__":
    main()
