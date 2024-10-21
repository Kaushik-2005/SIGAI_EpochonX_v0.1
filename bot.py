import os
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from document_generator import DocxGenerator
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai

class ProgressReportGenerator:
    def __init__(self):
        load_dotenv()
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
        
        # Updated prompt template to match the new progress report structure
        self.prompt_template = ChatPromptTemplate.from_messages([
            ("system", "You are an AI assistant that generates progress reports based on the given information. Format the report clearly using plain text. Ensure headings are in uppercase, and member names are emphasized with colons. Use indentation and line breaks for clean, readable structure."),
            ("human", """Please generate a progress report using the following information:
            REPORT PERIOD: {report_period}
            START DATE: {start_date}
            END DATE: {end_date}
            TEAM NAME/PROJECT: {team_name_or_project}
            PREPARED BY: {prepared_by}

            OVERVIEW
            ----------------
            {overview}

            TEAM MEMBER CONTRIBUTIONS
            ----------------
            {team_member_contributions}

            SIGN-OFF
            ----------------
            NAME: {sign_off_name}
            POSITION/ROLE: {sign_off_position}
            DATE: {sign_off_date}

            Please format the report in a professional manner, ensuring all sections are separated clearly and tasks are listed in an easy-to-read format.""")
        ])
        
        self.docx_generator = DocxGenerator()

    def get_user_input(self):
        inputs = {}
        
        print("Progress Report Generator")
        print("------------------------")
        
        inputs["report_period"] = input("Report Period (Weekly/Monthly): ")
        inputs["start_date"] = input("Start Date (YYYY-MM-DD): ")
        inputs["end_date"] = input("End Date (YYYY-MM-DD): ")
        inputs["team_name_or_project"] = input("Team Name/Project: ")
        inputs["prepared_by"] = input("Prepared By: ")
        inputs["overview"] = input("Overview: ")

        # Team Members
        no_of_members = int(input("Number of Team Members: "))
        team_member_contributions = []
        for i in range(no_of_members):
            print(f"\nMember {i + 1}")
            name = input(f"Name of Member {i + 1}: ")
            tasks_completed = input(f"Tasks Completed by Member {i + 1} (comma-separated): ")
            ongoing_tasks = input(f"Ongoing Tasks of Member {i + 1} (comma-separated): ")
            days_attended = input(f"Days Attended by Member {i + 1}: ")
            projects_working_on = input(f"Projects Working On by Member {i + 1}: ")
            hackathons_attended = input(f"Hackathons Attended by Member {i + 1}: ")
            
            member_info = (
                f"{name}:\n"
                f"  - Tasks Completed: {tasks_completed}\n"
                f"  - Ongoing Tasks: {ongoing_tasks}\n"
                f"  - Days Attended: {days_attended}\n"
                f"  - Projects Working On: {projects_working_on}\n"
                f"  - Hackathons Attended: {hackathons_attended}\n"
            )
            team_member_contributions.append(member_info)
        
        inputs["team_member_contributions"] = "\n".join(team_member_contributions)

        inputs["sign_off_name"] = input("Sign-off Name: ")
        inputs["sign_off_position"] = input("Sign-off Position/Role: ")
        inputs["sign_off_date"] = input("Sign-off Date (YYYY-MM-DD): ")

        return inputs

    def get_test_input(self):
        return {
            "report_period": "Weekly",
            "start_date": "2024-03-18",
            "end_date": "2024-03-24",
            "team_name_or_project": "ACM SIG AI",
            "prepared_by": "Kaushik",
            "overview": "This week, we focused on developing a chatbot and conducting AI workshops for freshers.",
            "team_member_contributions": (
                "Kaushik:\n"
                "  - Tasks Completed: Built a chatbot, Conducted workshop\n"
                "  - Ongoing Tasks: Learning NLP\n"
                "  - Days Attended: 5\n"
                "  - Projects Working On: AI chatbot, NLP toolkit\n"
                "  - Hackathons Attended: None\n"
            ),
            "sign_off_name": "Kaushik",
            "sign_off_position": "ACM/Mentor",
            "sign_off_date": "2024-03-24"
        }

    def generate_report(self, inputs):
        chain = self.prompt_template | self.model | StrOutputParser()
        progress_report = chain.invoke(inputs)
        return progress_report

    def generate_and_save_report(self, inputs, filename="progress_report.docx"):
        report_content = self.generate_report(inputs)
        self.docx_generator.generate(report_content, filename)
        return report_content

if __name__ == "__main__":
    generator = ProgressReportGenerator()
    
    # Use test inputs
    test_inputs = generator.get_test_input()
    
    print("Generating progress report with test inputs...")
    report = generator.generate_and_save_report(test_inputs)
    
    # print("\nGenerated Progress Report:")
    # print(report)

    # Uncomment the following lines if you want to test with user input
    # user_inputs = generator.get_user_input()
    # report = generator.generate_and_save_report(user_inputs, "user_progress_report.docx")
    # print("\nGenerated Progress Report:")
    # print(report)
