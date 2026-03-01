import re
from pathlib import Path

file_path = r'c:\git\mandarin-agents\scripts\generate_instructions.py'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add fallback to .github/agents for agent instructions
old_agent_fallback = '''    # Strategie 3: Fallback - zoek in prompt folder (klassieke methode)
    prompt_path = Path(prompt_file)
    prompt_dir = prompt_path.parent
    agent_file = prompt_dir / agent_file_name

    if agent_file.exists():
        print(f"[OK] Agent-instructies geladen: {agent_file}")
        with open(agent_file, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        print(f"INFO: Agent-instructies niet gevonden: {agent_file_name}")

    return None'''

new_agent_fallback = '''    # Strategie 3: Fallback - zoek in prompt folder (klassieke methode)
    prompt_path = Path(prompt_file)
    prompt_dir = prompt_path.parent
    agent_file = prompt_dir / agent_file_name

    if agent_file.exists():
        print(f"[OK] Agent-instructies geladen: {agent_file}")
        with open(agent_file, 'r', encoding='utf-8') as f:
            return f.read()

    # Strategie 4: Fallback - zoek in .github/agents
    github_agents_dir = Path(".github/agents")
    agent_file = github_agents_dir / agent_file_name
    if agent_file.exists():
        print(f"[OK] Agent-instructies geladen: {agent_file}")
        with open(agent_file, 'r', encoding='utf-8') as f:
            return f.read()
            
    # Strategie 5: Fallback - zoek in repo_root/artefacten
    repo_root = Path(__file__).resolve().parent.parent
    artefacten_path = repo_root / "artefacten"
    if artefacten_path.exists():
        for agent_folder in artefacten_path.rglob(f"*.{agent_naam}"):
            if agent_folder.is_dir():
                agent_contracten_folder = agent_folder / "agent-contracten"
                agent_file = agent_contracten_folder / agent_file_name
                if agent_file.exists():
                    print(f"[OK] Agent-instructies geladen: {agent_file}")
                    with open(agent_file, 'r', encoding='utf-8') as f:
                        return f.read()
                agent_file = agent_folder / agent_file_name
                if agent_file.exists():
                    print(f"[OK] Agent-instructies geladen: {agent_file}")
                    with open(agent_file, 'r', encoding='utf-8') as f:
                        return f.read()

    print(f"INFO: Agent-instructies niet gevonden: {agent_file_name}")
    return None'''

content = content.replace(old_agent_fallback, new_agent_fallback)

# Add fallback to repo_root/artefacten for charter
old_charter_fallback = '''    # Strategie 3: Fallback - zoek in prompt folder (klassieke methode)
    prompt_path = Path(prompt_file)
    prompt_dir = prompt_path.parent
    charter_file = prompt_dir / charter_file_name

    if charter_file.exists():
        print(f"[OK] Charter geladen: {charter_file}")
        with open(charter_file, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        print(f"INFO: Charter niet gevonden (optioneel): {charter_file_name}")

    return None'''

new_charter_fallback = '''    # Strategie 3: Fallback - zoek in prompt folder (klassieke methode)
    prompt_path = Path(prompt_file)
    prompt_dir = prompt_path.parent
    charter_file = prompt_dir / charter_file_name

    if charter_file.exists():
        print(f"[OK] Charter geladen: {charter_file}")
        with open(charter_file, 'r', encoding='utf-8') as f:
            return f.read()
            
    # Strategie 4: Fallback - zoek in repo_root/artefacten
    repo_root = Path(__file__).resolve().parent.parent
    artefacten_path = repo_root / "artefacten"
    if artefacten_path.exists():
        for agent_folder in artefacten_path.rglob(f"*.{agent_naam}"):
            if agent_folder.is_dir():
                charter_file = agent_folder / charter_file_name
                if charter_file.exists():
                    print(f"[OK] Charter geladen: {charter_file}")
                    with open(charter_file, 'r', encoding='utf-8') as f:
                        return f.read()

    print(f"INFO: Charter niet gevonden (optioneel): {charter_file_name}")
    return None'''

content = content.replace(old_charter_fallback, new_charter_fallback)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Done')
