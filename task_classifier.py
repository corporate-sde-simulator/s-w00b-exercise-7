"""
Task Type Classifier — identify the task type from clues.

For each scenario, type the correct task type:
  'BF' = Bug Fix
  'FS' = Feature Ship
  'MT' = Maintenance
  'DB' = Debugging

Run: python task_classifier.py
"""

scenarios = [
    {
        'id': 1,
        'description': "TICKET says 'Bug Fix'. You open src/ and see # BUG: comments pointing to wrong logic.",
        'clue': "Markers tell you exactly where to look.",
        'answer': 'BF',
    },
    {
        'id': 2,
        'description': "TICKET says 'Feature Ship'. You see // TODO: Implement stubs with detailed specs.",
        'clue': "Empty methods waiting for you to fill in.",
        'answer': 'FS',
    },
    {
        'id': 3,
        'description': "TICKET says 'Maintenance'. You see # TODO (code review): comments flagging bad practices.",
        'clue': "Code works but is messy — your job is to clean it up.",
        'answer': 'MT',
    },
    {
        'id': 4,
        'description': "TICKET says 'Debugging'. No markers in the code at all. Ticket describes symptoms.",
        'clue': "You have to trace the code and find the problem from behavior alone.",
        'answer': 'DB',
    },
    {
        'id': 5,
        'description': "Hotfix alert! Single file, JIRA header embedded in comments, # BUG: marker, 15-min SLA.",
        'clue': "High pressure, single file, direct fix.",
        'answer': 'BF',
    },
    {
        'id': 6,
        'description': "TICKET says the service is returning 500 errors. No markers. Logs show timeout spikes.",
        'clue': "Symptom-based investigation required.",
        'answer': 'DB',
    },
]

if __name__ == '__main__':
    type_names = {'BF': 'Bug Fix', 'FS': 'Feature Ship', 'MT': 'Maintenance', 'DB': 'Debugging'}
    score = 0
    print("\n--- Task Type Classifier ---\n")
    for s in scenarios:
        print(f"Scenario {s['id']}:")
        print(f"  {s['description']}")
        print(f"  Clue: {s['clue']}")
        user_answer = input(f"  Your answer (BF/FS/MT/DB): ").strip().upper()
        if user_answer == s['answer']:
            print(f"  Correct! ({type_names[s['answer']]})\n")
            score += 1
        else:
            print(f"  Wrong. Correct answer: {s['answer']} ({type_names[s['answer']]})\n")

    print(f"Score: {score}/6")
    if score >= 5:
        print("Excellent! You can identify task types quickly.")
    else:
        print("Review REFERENCE.md and try again.")
