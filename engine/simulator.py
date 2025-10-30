import random

def run_simulation(scenario):
    print("\n--- CAIO Roleplay Simulation ---")
    print(f"Scenario: {scenario['title']}")
    print(f"Context: {scenario['context']}")
    
    for step in scenario["steps"]:
        print("\nAI Tutor Prompt:")
        print(step["prompt"])
        user = input("Your response: ")
        print(f"Smart feedback: {random.choice(step['feedback'])}")

    score = random.randint(70, 100)
    print(f"\n✅ Simulation complete — YOUR SCORE: {score}%")
    return score
