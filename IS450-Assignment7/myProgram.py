"""Basketball Score Tracker - BAN 701 Assignment 7."""


def get_score(team_name):
    """Ask for a nonnegative whole-number score."""
    while True:
        entry = input(f"Enter the score for {team_name}: ")
        try:
            score = int(entry)
            if score >= 0:
                return score
            print("Please enter a score of 0 or higher.")
        except ValueError:
            print("Please enter a whole number.")


def main():
    print("=== Basketball Score Tracker ===")
    team_one = input("Enter the first team's name: ").strip() or "Team 1"
    team_two = input("Enter the second team's name: ").strip() or "Team 2"

    score_one = get_score(team_one)
    score_two = get_score(team_two)

    print("\n=== Final Score ===")
    print(f"{team_one}: {score_one}")
    print(f"{team_two}: {score_two}")

    if score_one > score_two:
        print(f"Winner: {team_one} by {score_one - score_two} points!")
    elif score_two > score_one:
        print(f"Winner: {team_two} by {score_two - score_one} points!")
    else:
        print("The game ended in a tie!")


if __name__ == "__main__":
    main()
