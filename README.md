🤖 HR Helpdesk Chatbot

An AI-powered HR Helpdesk Chatbot built with Python (Tkinter + Pandas) that helps employees quickly find answers to common HR queries such as salary details, leaves, allowances, and company policies.

This chatbot connects with an employee dataset (CSV file) and responds to both general and employee-specific queries in a chat-like GUI interface.

✨ Features

✅ Interactive Chatbot GUI – User-friendly interface with modern design
✅ Employee Authentication – Secure login with Employee ID verification
✅ Employee Info Retrieval – Fetch salary, leave balance, and allowances directly from the dataset
✅ General HR Queries – Get instant answers for company policies, holidays, salary date, etc.
✅ Smart Responses – Handles casual greetings & farewells gracefully
✅ Exit Confirmation – Prevents accidental closures with confirmation dialogs


🚀 Replace these placeholders with your real screenshots

🔹 Chatbot Interface
🔹 Employee ID Login

🛠️ Tech Stack

Python 🐍
Tkinter – GUI Framework
Pandas – Employee data handling
CSV File – Employee dataset storage

📂 Project Structure
HR-Helpdesk-Chatbot/
│── employees_dataset.csv      # Employee details dataset
│── chatbot.py                 # Main chatbot GUI code
│── responses.py               # Predefined HR responses
│── README.md                  # Project documentation

⚡ Installation & Usage
🔹 1. Clone the Repository
git clone https://github.com/your-username/HR-Helpdesk-Chatbot.git
cd HR-Helpdesk-Chatbot

🔹 2. Install Dependencies
Make sure you have Python 3.x installed. Then run:
pip install pandas

🔹 3. Add Employee Dataset
Ensure employees_dataset.csv is present in the project root folder. Example format:

empid	name	basic_salary	grade_pay	DA	home_rent	convience_allowance	absent	earned_leave	casual_leave	maternity_leave	washing_allowance
E001	Ayush P	40000	5000	2000	6000	1500	2	5	3	0	300

🔹 4. Run the Chatbot
python chatbot.py

💬 Example Conversations
User: "Hello"
Bot: "Hi there! How can I assist you today?"

User: "What is my salary?"
Bot: "Your basic salary is 40000."

User: "Bye"
Bot: "Goodbye! Have a great day!"

🚀 Future Enhancements
🌐 Connect with real-time HRMS system instead of CSV
🤝 Integration with Slack / MS Teams
📊 Generate employee payslip reports
🧠 Add NLP-based understanding for natural queries
🤝 Contributing

Contributions are welcome! 🎉
If you’d like to add features or fix issues, please fork the repo and submit a pull request.

📜 License
This project is licensed under the MIT License – you’re free to use, modify, and distribute.

👨‍💻 Author
Ayush Pandit

🚀 Passionate about AI, ML & Python
📚 BCA Student | 8+ CGPA
💼 Aspiring AI/ML Engineer
🔗 Connect with me on:
www.linkedin.com/in/ayush-pandit-543890292



✨ Made with Python & ❤️ by Ayush Pandit
