import os
from dotenv import load_dotenv
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
os.environ["NVIDIA_API_KEY"] = os.getenv("NVIDIA_API_KEY")

model = ChatNVIDIA(model="meta/llama3-70b-instruct")

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are an AI assistant that generates progress reports based on the given information."),
    ("human", """Please generate a progress report using the following information:
    Report Period: {report_period}
    Start Date: {start_date}
    End Date: {end_date}
    Team Name/Project: {team_name_or_project}
    Prepared By: {prepared_by}
    Overview: {overview}
    Team Member Contributions: {team_member_contributions}
    Key Achievements: {key_achievements}
    Challenges and Issues: {challenges_and_issues}
    Action Items for Next Period: {action_items_for_next_period}
    Additional Notes: {additional_notes}
    Sign-off Name: {sign_off_name}
    Sign-off Position/Role: {sign_off_position}
    Sign-off Date: {sign_off_date}

    Please format the report in a professional manner, including all provided information.""")
])

def get_test_input():
    return {
        "report_period": "Weekly",
        "start_date": "2024-03-18",
        "end_date": "2024-03-24",
        "team_name_or_project": "ACM SIG AI",
        "prepared_by": "Kaushik",
        "overview": "This week, we focused on developing a chatbot and conducting AI workshops for freshers.",
        "team_member_contributions": "Kaushik: Tasks Completed - Built a chatbot, Conducted workshop; Ongoing Tasks - Learning NLP; Challenges - None; Next Steps - Finish NLP course",
        "key_achievements": "Successfully built a functional chatbot, Recruited new members",
        "challenges_and_issues": "No major issues encountered",
        "action_items_for_next_period": "Plan advanced AI workshops, Improve chatbot functionality",
        "additional_notes": "Team morale is high, and we're excited about upcoming projects.",
        "sign_off_name": "Kaushik",
        "sign_off_position": "ACM/Mentor",
        "sign_off_date": "2024-03-24"
    }

def generate_progress_report(inputs):
    chain = prompt_template | model | StrOutputParser()
    progress_report = chain.invoke(inputs)
    return progress_report

if __name__ == "__main__":
    # Use test inputs
    # test_inputs = get_test_input()
    
    # print("Generating progress report with test inputs...")
    # report = generate_progress_report(test_inputs)
    
    # print("\nGenerated Progress Report:")
    # print(report)

    # Uncomment the following lines if you want to test with user input
    user_inputs = get_user_input()
    report = generate_progress_report(user_inputs)
    print("\nGenerated Progress Report:")
    print(report)