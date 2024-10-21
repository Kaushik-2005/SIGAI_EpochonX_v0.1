import os
from dotenv import load_dotenv
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
os.environ["NVIDIA_API_KEY"] = os.getenv("NVIDIA_API_KEY")

model = ChatNVIDIA(model="meta/llama3-70b-instruct")

prompt_template = ChatPromptTemplate.from_template("""
{
    "report_period": "{report_period}",
    "start_date": "{start_date}",
    "end_date": "{end_date}",
    "team_name_or_project": "{team_name_or_project}",
    "prepared_by": "{prepared_by}",
    "overview": "{overview}",
    "team_member_contributions": [
        { "member_name": "{member_1_name}", "tasks_completed": {member_1_tasks_completed}, "ongoing_tasks": {member_1_ongoing_tasks}, "challenges_encountered": "{member_1_challenges}", "next_steps": {member_1_next_steps} }
    ],
    "key_achievements": {key_achievements},
    "challenges_and_issues": {challenges_and_issues},
    "action_items_for_next_period": "{action_items_for_next_period}",
    "additional_notes": "{additional_notes}",
    "sign_off": { "name": "{sign_off_name}", "position_or_role": "{sign_off_position}", "date": "{sign_off_date}" }
}
""")

def get_user_input():
    inputs = {}
    
    print("Progress Report Generator")
    print("------------------------")
    
    # General Information
    inputs["report_period"] = input("Report Period (Weekly/Monthly): ")
    inputs["start_date"] = input("Start Date (YYYY-MM-DD): ")
    inputs["end_date"] = input("End Date (YYYY-MM-DD): ")
    inputs["team_name_or_project"] = input("Team Name/Project: ")
    inputs["prepared_by"] = input("Prepared By: ")
    inputs["overview"] = input("Overview: ")

    # Team Members
    no_of_members = int(input("Number of Team Members: "))
    for i in range(no_of_members):
        print(f"\nMember {i + 1}")
        inputs[f"member_{i+1}_name"] = input(f"Name of Member {i + 1}: ")
        inputs[f"member_{i+1}_tasks_completed"] = input(f"Tasks Completed by Member {i + 1} (comma-separated): ").split(',')
        inputs[f"member_{i+1}_ongoing_tasks"] = input(f"Ongoing Tasks of Member {i + 1} (comma-separated): ").split(',')
        inputs[f"member_{i+1}_challenges"] = input(f"Challenges Encountered by Member {i + 1}: ")
        inputs[f"member_{i+1}_next_steps"] = input(f"Next Steps for Member {i + 1} (comma-separated): ").split(',')

    # Additional Details
    inputs["key_achievements"] = input("Key Achievements (comma-separated): ").split(',')
    inputs["challenges_and_issues"] = input("Challenges and Issues (comma-separated): ").split(',')
    inputs["action_items_for_next_period"] = input("Action Items for Next Period (comma-separated): ").split(',')
    inputs["additional_notes"] = input("Additional Notes: ")

    # Sign-Off
    inputs["sign_off_name"] = input("Sign-off Name: ")
    inputs["sign_off_position"] = input("Sign-off Position/Role: ")
    inputs["sign_off_date"] = input("Sign-off Date (YYYY-MM-DD): ")

    return inputs

def generate_progress_report(inputs):
    chain = prompt_template | model | StrOutputParser()
    progress_report = chain.invoke(inputs)
    return progress_report

if __name__ == "__main__":
    user_inputs = get_user_input()
    report = generate_progress_report(user_inputs)
    print("\nGenerated Progress Report:")
    print(report)