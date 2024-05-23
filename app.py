from flask import Flask, jsonify, request, render_template, session
import os
import requests
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

api_key = os.environ.get("AIzaSyBkDM42BKsMd0BBFreeg2fa4zMsiC2gCX0")

from google.generativeai import GenerativeModel
import google.generativeai as genai

genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="gemini-pro")

def get_ai_service_response(user_message: str) -> dict:
    """Get AI response from external service"""
    ai_service_endpoint = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyBkDM42BKsMd0BBFreeg2fa4zMsiC2gCX0"
    test = {
                "contents": [
            {
            "parts": [
                                {
                    "text": "input: Where can I find my class schedule?"
                },
                {
                    "text": "output: You can find your class schedule at https://www.timetableplus.com/ucts/index.php/site/student."
                },
                {
                    "text": "input: Where can I find my course materials?"
                },
                {
                    "text": "output: You can find your course materials on Google Classroom."
                },
                {
                    "text": "input: How do I access campus WiFi ?"
                },
                {
                    "text": "output: The password for the campus WiFi is Student123."
                },
                {
                    "text": "input: Can you tell me where the admin office is located?"
                },
                {
                    "text": "output: The admin office is located at Block 3, which is located on the left side of the main entrance to campus."
                },
                {
                    "text": "input: How do I obtain a student ID card and what is it used for ?"
                },
                {
                    "text": "output: You can obtain your student ID card from AARD. It can be used for entering the library and office. It is also needed for your final exam."
                },
                {
                    "text": "input: Where can I find information about campus events and activities ?"
                },
                {
                    "text": "output: You can find information about campus events and activities on the UTS official website or on the social media of UTS, such as Facebook and Instagram. You can also pay attention to your Gmail."
                },
                {
                    "text": "input: What dining options are available on campus ?"
                },
                {
                    "text": "output: The cafeteria in the campus will be open until 9pm and you can also get your meal below the hostel."
                },
                {
                    "text": "input: Can you explain how to use the library and borrow books ?"
                },
                {
                    "text": "output: You can use your student ID card to scan for entry into the library. Then, you need to put your belongings on the cabinets that are provided under the stairs, which are located on the left side of the entrance. You can borrow the books from the library.To borrow the books, you will need a student ID."
                },
                {
                    "text": "input: What are the transportation options to get around campus and surrounding areas?"
                },
                {
                    "text": "output: We provide the van and bus for the students who live in the hostel. If you want to go to other places, you can book a “Grab” or “Maxim” car."
                },
                {
                    "text": "input: What sports facilities are open to students?"
                },
                {
                    "text": "output: Gym room, badminton court, table tennis room, basketball court."
                },
                {
                    "text": "input: How do I join a club or student organisation that interests me?"
                },
                {
                    "text": "output: You can find the president or member of the club when there are club booths behind the LTC. Or get invited by the members."
                },
                {
                    "text": "input: Are there any orientation programs or workshops for new students?"
                },
                {
                    "text": "output: Yes, we have an orientation programme for every new semester student."
                },
                {
                    "text": "input: Where can I go for help with financial aid and student loans?"
                },
                {
                    "text": "output: You can find and contact the financial department, or you can kindly email sdscfinaid@uts.edu.my. For updated information regarding financial assistance, kindly visit https://sdsc.uts.edu.my/."
                },
                {
                    "text": "input: How do I set up my university email account and access the online portal?"
                },
                {
                    "text": "output: You can set up your university email account when you have your student ID."
                },
                {
                    "text": "input: Can you explain the process for registering for classes?"
                },
                {
                    "text": "output: First, you need to log in to your Oculus. Then, you go to “Course Registration First Submission,” which is under the student portal. You register the courses that you take for that semester."
                },
                {
                    "text": "input: How do I learn about campus safety procedures and emergency protocols?"
                },
                {
                    "text": "output: You can learn that from the UTS handbook or during the orientation."
                },
                {
                    "text": "input: Can you recommend a study spot or quiet spot on campus?"
                },
                {
                    "text": "output: I think the library will be the best spot for you. It has air conditioning, free charging space, and is quiet."
                },
                {
                    "text": "input: How do I meet with my academic advisor and what can they help me with?"
                },
                {
                    "text": "output: Just simply email him."
                },
                {
                    "text": "input: How do I access with recreational activities on campus?"
                },
                {
                    "text": "output: I think you should email SDSC."
                },
                {
                    "text": "input: Can you provide information about scholarships or financial aid opportunities\navailable to new students?"
                },
                {
                    "text": "output: You can find and contact the financial department, or you can kindly email sdscfinaid@uts.edu.my. For updated information regarding financial assistance, kindly visit https://sdsc.uts.edu.my/."
                },
                {
                    "text": "input: Where can I check my results?"
                },
                {
                    "text": "output: In your oculus website."
                },
                {
                    "text": "input: What resources are available for students interested in participating in an exchange programme?"
                },
                {
                    "text": "output: You can email your HOP for more information. You can exchange with the university that has a corporation with our university."
                },
                {
                    "text": "input: How do I get academic advice or counselling services to choose my major or plan my academic path?"
                },
                {
                    "text": "output: You can email the counsellor executive, psychology and counselling unit, and student development and services centre (SDSC)."
                },
                {
                    "text": "input: How can I access academic counselling services?"
                },
                {
                    "text": "output: You can email the counsellor executive, psychology and counselling unit, and student development and services centre (SDSC)."
                },
                {
                "text": "output: Welcome to University of Technology Sarawak (UTS), one of the new breed of technological based universities in the country. Founded in 2013, UTS is the only university which is wholly owned by the Sarawak State Government.\n\nLocated in the heart of Borneo, UTS offers a broad range of professional and industry-linked academic programmes that are relevant to the unique requirements of Sarawak in particular and Malaysia in general. Therefore, we are proud to be recognized as the only “home-grown” TVET university in Sarawak with the aim to produce an educated and highly skilled human capital for the new and emerging industries.\n\nUTS also prides itself as the only university in the world being awarded the prestigious Platinum ratings in Green Building Index (GBI) for its campus design in promoting sustainability in the built environment and energy utilization. The campus design is very impressive, stunningly beautiful and remarkably spectacular. This modern setting within the enclosure of the rainforest and nature will provide the most conducive learning environment for our students.\n\nThe University has invested heavily in teaching-learning facilities, especially state-of-the-art laboratories equipment, ICT infrastructure and services, and other resources for research and development (R&D). Our R&D activities are very closely linked and collaborated with industry partners and government agencies.\n\nIn recent years we have been embarking on our internationalization programmes to include student mobility, staff exchange, academic articulation arrangement and joint research projects with universities from United Kingdom, Australia, Europe, Japan, China, Korea, Taiwan, India and ASEAN countries.\n\nWe would like to welcome you and to be part of this energetic and highly motivated campus community that will unleash your full potential to realize your dreams.\n\nI am delighted to be part of this promising new university. I wish to work closely with all staff and students in making UTS a great institution of academic excellence with dignified character and values.\n\nProf Datuk Dr Khairuddin Ab Hamid\nVice Chancellor\n\nAbout University\nUniversity of Technology Sarawak (UTS) is the culmination of the State of Sarawak’s vision and commitment in establishing a world-class institution of higher learning to spearhead the development and production of technical human resource for the Sarawak Corridor of Renewable Energy (SCORE).\n\nUTS is committed to facilitating students’ access to an affordable world-class university education that nurtures creative and entrepreneurial leaders through a broad education in science and technology while combining the career benefits of an applied approach for SCORE-related research and career opportunities.\n\nSituated in Sibu, one of the main gateways into SCORE, UTS campus is equipped with the latest state-of-the-art facilities to facilitate teaching, learning and research activities necessary in the production of graduates required by the industries within SCORE.\n\nIn addition, UTS will be complemented by its own Science & Technology Park, which will bring about vast research and entrepreneurial opportunities through local and international industrial and educational collaborations.\n\nThrough its close collaboration with Universiti Kuala Lumpur, one of Malaysia’s leading technical universities with over 20,000 students across the country, UTS aims to complement the growth and fulfil the human resource and industrial needs of SCORE.\n\nUTS now runs Transfer Degree Programme with four universities namely Murdoch University from Australia; University of Essex and University of Birmingham from the United Kingdom; and University of Canterbury from New Zealand.\n\nVision : Our vision is to be a global technical university founded on science and technology.\nMission : Our mission is to provide world-class educational programs and learning environment to nurture creative and entrepreneurial leaders through a broad yet specialised education in science and technology.\nCore Values : The core values that guide us in our mission are Commitment, Integrity, Caring, Enterprising, and Green."
                },
                {
                "text": "input: Offered Schools and programmes in UTS"
                },
                {
                "text": "output: Offered Schools & Programmes\n\nCurrently UCTS offers 29 programmes under six schools and seven new programmes are still pending at Malaysian Qualification Agemcy (MQA), Professional Bodies or MOHE’s License approval. List of programmes offered under six schools are as follows:\n\nSchool of Foundation Studies:\nFoundation in Sciences\nFoundation in Arts\n\nSchool of Business and Management:\nBachelor of Business Administration (Hons)\nBachelor of Accountancy (Hons)\nBachelor of Business (Hons) in Marketing\nBachelor of Technology Management (Hons)\n\nSchool of Built Environment:\nBachelor of Quantity Surveying (Hons)\nBachelor of Science (Hons) in Architecture\nBachelor of Arts (Hons) in Interior Design\n\nSchool of Computing and Creative Media:\nBachelor of Computer Science (Hons)\nBachelor of Arts (Hons) in Industrial Design\nBachelor of Arts (Hons) in Creative Digital Media\n\nSchool of Engineering and Technology:\nBachelor of Civil Engineering (Hons)\nBachelor of Mechanical Engineering (Hons)\nBachelor of Electrical Engineering (Hons)\nBachelor of Food Technology (Hons)\nBachelor of Engineering Technology in Electrical and Electronic (Hons)\n\nSchool of Postgraduate Studies:\nMaster of Engineering (Research Mode)\nMaster of Science in Business Management (Research Mode)\nMaster of Business Administration (MBA)\nMaster of Project Management\nMaster of Architecture\nMaster of Science in Applied Sciences (Research Mode)\nDoctor of Philosophy (PhD) in Engineering\nDoctor of Philosophy (PhD) in Business Management\nDoctor of Philosophy (PhD) in Applied Science\n\nFuture Programmes:\nBachelor of Science in Construction and Property Management\nBachelor of Mobile Game Development (Hons)\nMaster of Construction Management and Economics\nMaster of Science in Architecture\nMaster of Science in Construction Management\nDoctor of Philosophy in Architecture\nDoctor of Philosophy in Construction Management"
                },
                {
                "text": "input: Management team(only show the name)"
                },
                {
                "text": "output: Management Team Vice Chancellor / President : Prof. Datuk Dr. Khairuddin Ab. Hamid, PhD Electronic Systems Eng. (Essex), MSc. Electrical Eng (Hawaii), B. Electrical Eng. (UTM) Deputy Vice Chancellor (Academic)Prof. Ir. Ts. Dr. Mohammad Shahril Bin OsmanPhD, B. Eng (Hons) Mechanical Engineering (Loughborough) BursarDr. Rabuan Bin MantinePhD in Finance (UNIMAS), Master of Business Administration (OHIO), Adv. Diploma in Accountancy (UiTM), Chartered Accountancy (M) RegistrarMr Jimmy De Rozario @ Abdul Rahman, CHRC, CHRA, AMCBA HR (UPM), Dip. Public Admin (UiTM)  Dean, School of Engineering and TechnologyAssociate Professor Dr. Dayang Siti Hazimmah Binti AliPhD Civil Engineering in Construction Materials (UMP), MSc. in Materials Engineering (USM), B. Eng in Materials Engineering (USM) Dean, School of Built EnvironmentSr. Dr. Kan Fock KuiPhD Quantity Surveying (UTM), MSc in Construction Management (Bath), Dip in Technology (Building) (TARC) Dean, School of Business and ManagementAssoc. Prof. Dr Winnie Wong Poh MingPhD Marketing (UNIMAS), MBA (UMS), B. Ed (Education with Economics) Dean, School of Computing & Creative MediaTs. Dr. Alan Ting Huong YongPhD (MMU) Dean, School of Foundation StudiesMr Muhammad Afif Abdul RaniMaster of Science (Hons) in Applied Physics and Master in Theoretical Physics, Bachelor of Science (Hons) Applied Physics Dean, School of Postgraduate StudiesAssoc. Prof. Dr. Mohd Zainal Munshid bin HarunDoctor of Business Administration (DBA) (UUM), Master of Business Administration (UUM), BA (Hons) Business Administration & Commerce, De Montfort University, Higher National Diploma (Business and Finance), De Montfort University Director, Centre for Quality AssuranceDr. Sim Siew LingPhD in Business Management (UTS), MBA in Venture Capital Management (UTM), Bachelor of Business Administration (Finance) (UPM) Director, Centre for Research & DevelopmentAssoc. Prof. Dr Mohd Zahid bin AbidinPhD Food Technology (UiTM), MSc Foodnology (USM), BSc Food Technology (USM)  Director, Centre of University Courses and Innovative Learning Mdm Nadira binti Abdul RahmanMSc in Human Resource Development (UNIMAS), Bachelor of Arts in English Language (UPM)  Director, Centre for Continuing Education & Professional Development Assoc. Prof. Dr Ramli RashidiPhD TEVT (Bremen/UTHM), MSc HRD (UPM), B. Eng E&E (Brighton, England)  Director, Centre for International RelationsTs. Gary Loh Chee Wyai MSc in Computer Science (UNIMAS), Bachelor of Computer Science (Hons) (UNIMAS)  Director, Centre of Publication (UTS Publisher)Associate Professor Dr. Muhammad Firdaus Abong Bin AbdullahPhD., MSc. (Industrial Design), Loughborough University, UK, B.A. (Art & Design), UiTM Chief Librarian Academic Resource CentreMs Roselind Ak DuatBachelor Library & Information (UiTM)  Head of Corporate & Relations DepartmentMr Mohd Ian Daim bin MahmudBachelor of Corporate Administration (Hons) (UITM) Head of Human Capital & Admin DepartmentMdm Nurfaezah binti SharifBachelor in Human Resource Development (UNIMAS) Head of Academic Affairs & Registry DepartmentMdm Aspa Aida binti MohamadBachelor Science in Human Development (UPM) Head of Information TechnologyMr Shukri Abdul RahmanB. Computer Info System Eng (IIUM)  Head of Maintenance & SecurityMr Lau Hwi SungB. Commerce (Windsor, Canada)  Head of Account / FinanceMs Su Yew ChingB. Commerce Major in Accounting (Queensland, Australia), CA (MIA), CPA Australia Head of Student Development & Services Mr Lu Yew KingB. Eng Mechanical (Brighton, England)  Head of Marketing & Student Recruitment (Kuching)Mr Lau Wee MingMaster of Science (Marketing), B. of Business Management (Marketing) Head of Marketing & Student Recruitment (Sibu)Mr Shahminan Bin SamionB. of Business Administration (Hons) Majoring in Human Resource Management"
                },
                {
                "text": "input: Office"
                },
                {
                "text": "output: At the Vice Chancellor'\''s Office, Prof Datuk Dr Khairuddin Ab. Hamid leads as Vice Chancellor, overseeing academic affairs and research. Nurhajijah binti Mohammad serves as the Secretary to the Vice Chancellor, ensuring smooth operations.In the Deputy Vice Chancellor'\''s Office, Prof. Ir. Ts. Dr. Mohammad Shahril bin Osman holds the position of Deputy Vice Chancellor (Academic), focusing on academic excellence and student development. Radhika anak Rahman supports administrative functions as an Admin Officer."
                },
                {
                "text": "input: Callender foundation"
                },
                {
                "text": "output: Foundation Studies Academic Calendar, Session 2023-2024:SEMESTER ONERegistration & Orientation: 20.06.23 - 23.06.23Classes: 26.06.23 - 08.10.23Mid-Semester Break: 14.08.23 - 20.08.23Exams: 16.10.23 - 29.10.23SEMESTER TWORegistration & Orientation: 14.11.23 - 17.11.23Classes: 20.11.23 - 03.03.24Mid-Semester Break: 08.01.24 - 14.01.24Exams: 11.03.24 - 24.03.24SEMESTER THREEClasses: 15.04.24 - 02.06.24Exams: 10.06.24 - 16.06.24"
                },
                {
                "text": "input: Entry qualification"
                },
                {
                "text": "output: UTS offers diverse programs with entry requirements spanning SPM/O-levels to UEC for Foundation studies, while undergraduate and postgraduate programs have specific entry criteria based on fields like engineering, business, and arts. Postgraduates, including Master'\''s and Ph.D. applicants, need to meet CGPA and experience prerequisites. UTS also provides an APEL pathway for individuals aged 21 and above without formal qualifications, offering an alternative entry method through portfolio assessment aptitude tests conducted by MQA."
                },
                {
                "text": "input: Tution fee"
                },
                {
                "text": "output: For Local StudentsFoundation ProgrammesProgrammesTotal Fees Per Year (RM)*Foundation in Science10,000 Foundation in Arts10,000* Full sponsorship to cover the tuition fees for the Foundation Programmes are available for qualified Malaysian students (subject to terms and conditions).Undergraduate ProgrammesThe tuition fees payable for undergraduate programmes are based on actual credits taken for the semester. The semester fees shown below are approximate figures only. Students with a recognised Diploma qualification for entry can apply for credit exemptions following the rules and guidelines established by the Malaysian Qualifications Agent (MQA).ProgrammeCreditsYearsRegular Fees(For other Malaysians)50% Bursary Scheme(For Sarawakian)80% Bursary Scheme B40(For Sarawakian B40)   Total (RM)Per Year (RM)Total (RM)Per Year (RM)Total (RM)Per Year (RM)School of Engineering and Technology (SET)Bachelor of Civil Engineering (Hons)  135470,25517,56435,1288,782 14,051 3,513Bachelor of Mechanical Engineering (Hons) 136474,01518,50437,0089,25214,8033,701Bachelor of Electrical Engineering (Hons)  135470,89517,72435,4488,86214,1793,545Bachelor of Food Technology (Hons)  129 460,75015,18830,3757,59412,1503,038Bachelor of Science in Occupational Safety and Health (Hons)  120 357,84019,28028,9209,64011,5683,856School of Business and Management (SBM)Bachelor of Business Administration (Hons) 120 348,65016,21724,325 8,1089,730 3,243Bachelor of Accountancy (Hons)126346,43015,47723,2157,7389,2863,095Bachelor of Business (Hons) in Marketing 120348,94016,31324,4708,1579,7883,263Bachelor of Technology Management (Hons)121 348,79016,26324,3958,1329,7583,253School of Built Environment (SBE)Bachelor of Quantity Surveying (Hons)  1283.554,21015,48927,1057,74410,8423,098Bachelor of Science in Architecture (Hons)120 365,02021,67332,51010,83713,0044,335Bachelor of Arts (Hons) in Interior Design120 3.564,87018,53432,4359,26712,9743,707Bachelor of Science (Honours) in Property and Construction Management1223.552,62015,03526,3107,51710,5243,007School of Computing and Creative Media (SCM)Bachelor of Computer Science  (Hons)1263.552,44014,98326,2207,49110,4882,997Bachelor of Arts in Industrial Design (Honours)120356,71018,90328,3559,45211,3423,781Bachelor of Arts (Hons) in Creative Digital Media120 3.564,89518,54132,4489,27112,9793,708Bachelor of Mobile Game Development (Hons)120 3.565,21018,63132,6059,31613,0423,726* Note : Actual fees per semester for Bachelor Degrees will be based on credits taken by students for the particular semester. Figures shown in the year columns are only estimates.Study loan is available from PTPTN. The tuition fees above are only applicable to local / Malaysian students. For more details and information, please contact our Marketing Office at 084-367300.Postgraduate ProgrammesProgrammesTotal Course Fee– Full Time (RM)*Total Course Fee– Full TimeUnder UTS Scholarship(RM)*Total Course Fee– Part Time (RM)*Total Course Fee– Part TimeUnder UTS Scholarship(RM)*Master of Architecture (by Coursework)32,85017,000NILNILMaster of Project Management (by Coursework)21,95011,45022,70012,200Master of Business Administration (by Coursework)21,95011,45022,30011,800Master of Construction Management (by Coursework)20,95010,95021,60011,600Master of Science in Business Management10,3006,55010,7507,000Master of Science in Architecture10,3006,55010,7507,000Master of Science in Construction Management10,3006,55010,7507,000Master of Engineering12,3008,55014,75011,000Master of Science in Applied Sciences12,3008,55014,75011,000Master in Computing12,3008,55014,75011,000Doctor of Philosophy (PhD) in Business Management17,25011,00015,70010,450Doctor of Philosophy (PhD) in Architecture17,25011,00015,70010,450Doctor of Philosophy (PhD) in Construction Management17,25011,00015,70010,450Doctor of Philosophy (PhD) in Engineering21,25015,00021,70016,450Doctor of Philosophy (PhD) in Applied Sciences21,25015,00021,70016,450Doctor of Philosophy (PhD) in Computing21,25015,00021,70016,450NOTE:1. UTS Scholarship is only available for Sarawak citizens. It is only applicable within the minimum duration of study. students exceeding the minimum duration of study will have to pay the Basic Tuition Fee in full. *If the student could not go for viva-voce examination on Year 2 Semester 2 (full time) or Year 3 Semester 2 (part time), the student will be charged the total course fee for the following semesters.2. 1 year of study is equivalent to 2 long semesters ; NIL – Not In Listed3. Every students by Research mode is required to register for a compulsory subject : Research Methodology which is 3 credit hours.4. Other Fees are inclusive of: – Study Resources Fee (RM100 per semester) and – Security Deposit (RM250 payable upon registration, refundable).5. All the above fee excludes fee for research expenditure, recurring fess, dissertation/thesis re-examination fee, fee for appeal to review the examination results, fee for appeal for review of dissertation/thesis.For International StudentsFoundation Programmes Tuition Fees Duration (Years)Fees Per Year (RM)*Foundation in Science1  13,000.00Foundation in Arts1   13,000.00Undergraduate Programmes Tuition Fees Duration (Years)Fees Per Year (RM)*Bachelor of Civil Engineering (Hons)422,830.00Bachelor of Mechanical Engineering (Hons)422,455.00Bachelor of Electrical Engineering (Honours)423,045.00Bachelor of Food Technology (Hons)419,830.00Bachelor of Science in Occupational Safety and Health (Hons)325,064.00Bachelor of Business Administration (Hons)321,100.00Bachelor of Business (Hons) in Marketing321,227.00Bachelor of Accountancy (Honours)319,980.00Bachelor of Technology Management (Hons)321,160.00Bachelor of Quantity Surveying (Hons)3.520,114.00Bachelor of Science (Hons) in Architecture328,220.00Bachelor of Computer Science (Hons)3.519,743.00Bachelor of Arts in Industrial Design (Honours)324,563.00Bachelor of Arts (Hons) in Creative Digital Media3.528,110.00Bachelor of Mobile Game Development (Hons)3.524,210.00Postgraduate Programmes Tuition FeesDuration (Years)Total Fees  (RM)*Master of Architecture2±43,330.00Master of Business Administration1.5±30,000.00Master of of Project Management1.5±30,000.00Master of Science in Business Management 2±18,000.00Master of Engineering 2±19,500.00Doctor of Philosophy (PhD) in Engineering 3 ±32,000.00Doctor of Philosophy (PhD) in Applied Sciences 3 ±32,000.00Doctor of Philosophy (PhD) in Business Management 3 ±26,000.00Doctor of Philosophy (PhD) in Business Management 3 ±26,000.00"
                },
                {
                "text": "input: Bachelor of computer sciences"
                },
                {
                "text": "output: The Bachelor of Computer Science (Hons) program aims to produce ethical software engineers for the global market. Graduates gain skills for employment, communication, and lifelong learning. The curriculum covers theoretical principles, practical methodologies, problem-solving, and professional conduct. Entry requirements include Matriculation, STPM, Diploma, or equivalent qualifications focusing on mathematics and science subjects. Tuition fees are subject to change, with study loans available for local students. Contact the Marketing Office for more information."
                },
                {
                "text": "input: Who are you"
                },
                {
                "text": "output: I'm UTS CHAT BOT. What can i assist you today?"
                },
                {
                "text": "input: What is Transfer Degree Programme?"
                },
                {
                "text": "output: What is Transfer Degree Programme?\nIt is basically an inter-university arrangement whereby two or more universities agree to recognize part of the courses so that when the students proceed to transfer to the partner university they do not have to repeat the courses. They can get those credits recognized and transferred so that they can complete their study with a degree from our partner universities.\nUCTS now runs Transfer Degree Programme with five foreign universities namely:\nUniversity of Essex, the United Kingdom\nUniversity of Canterbury, New Zealand\nMurdoch University, Australia\nUniversity of Birmingham, the United Kingdom"
                },
                {
                "text": "input: Master in Computing"
                },
                {
                "text": "output: The Master in Computing program at UCTS offers high-level academic qualifications with intakes in March, June, September, and December. It empowers students to delve deep into their chosen computing field, fostering theoretical and practical contributions. Research specializations include Computer Science, Information Systems, Software Engineering, and more. The program duration ranges from 2 to 6 years, depending on full-time or part-time enrollment. Entry requirements include a Bachelor’s Degree in Computing or related areas with a minimum CGPA of 3.00, or equivalent qualifications recognized by the Malaysian Government. Applicants must submit a research proposal and familiarize themselves with the program details before applying. Prospective students are encouraged to contact potential supervisors before formal application. Tuition fees for local and international students are approximately RM 14,000.00 and RM 16,000.00 respectively. The program structure emphasizes individual supervised research, complemented by a Research Methodology Course. Upon completion, students submit a thesis for defense. For further information, contact the Programme Coordinator, Associate Professor Dr Tariq Zaman, at tariqzaman@uts.edu.my or visit the School of Postgraduate Studies website at https://uts.edu.my/schools/school-of-postgraduate-studies/."
                },
                {
                "text": "input: The Foundation in Arts Programme at UTS"
                },
                {
                "text": "output: The Foundation in Arts Programme at UTS is designed to equip students with fundamental knowledge and analytical skills in core Arts subjects such as Languages, Information Technology, and Mathematics, enabling them to pursue Bachelor’s degree programmes in various fields. The programme duration is one year. Upon completion, students will have mastered essential pre-university level areas, developed rational thinking, communication skills, and scientific reasoning. They will also be prepared to pursue Bachelor’s degrees and manage their time effectively. The programme structure includes core and elective courses covering subjects like Mathematical Analysis, Economics, Accounting, Marketing, Business Law, Multimedia, and more. Assessment methods include coursework and final examinations. The course synopsis provides an overview of each subject'\''s content and references for further study. Additionally, students must adhere to academic and conduct regulations outlined in the handbook."
                },
                {
                "text": "input: foundation in science progamme"
                },
                {
                "text": "output: FOUNDATION IN SCIENCE PROGRAMME GUIDEBOOKFifth Edition ©2022. UTS. ALL RIGHTS RESERVEDCONTENTSProgramme DescriptorProgramme ObjectivesProgramme Learning OutcomesProgramme StructureCourse Synopsis1.0 PROGRAMME DESCRIPTOR FOR FOUNDATION IN SCIENCE (FIS)Programme: Foundation in Science (FIS)Programme Code: R/010/3/0125Final Award: Certificate of Foundation in ScienceTeaching Institution: University of Technology SarawakStudy Duration: 1 year2.0 PROGRAMME OBJECTIVESProvide fundamental knowledge and analytical skills in science.Inculcate good communication, leadership, and social skills, along with high ethical attitude.3.0 PROGRAMME LEARNING OUTCOMESUpon completion, students will:Master fundamental knowledge in Mathematics and Science.Apply fundamental knowledge in problem-solving and laboratory experiments.Develop rational thinking, humanity, humility, and respect for lecturers.Understand the importance of academic integrity and effective communication.Acquire scientific reasoning and critical analysis skills across major fields.Gain necessary knowledge to pursue Bachelor’s degrees.Develop time management skills.4.0 PROGRAMME STRUCTUREYear 1, Semester 1: Core courses in Mathematics, Physics, Chemistry, English, Critical Thinking, and Event Management.Year 1, Semester 2: Core courses in Mathematics, Physics, Chemistry, English, and Elective courses.Year 1, Semester 3: Core courses in Mathematics, Physics, and Computing.5.0 COURSE SYNOPSISCourses cover Mathematics, Physics, Chemistry, English, Critical Thinking, Event Management, Bahasa Kebangsaan, and Computing.Each course includes assessments through coursework and final examinations.References provided for each course for further study.Note: The guidebook emphasizes academic rigor, skill development, and preparation for further studies or careers in science-related fields. Students are encouraged to adhere to academic integrity and campus rules."
                },
                {
                "text": "input: ACADEMIC CALENDAR FOR UNDERGRADUATES"
                },
                {
                "text": "output: ACADEMIC CALENDAR FOR UNDERGRADUATES \n SESSION 2024-2025\nSEPTEMBER SEMESTER\nRegistration/Orientation 4 days 17.09.2024 - 20.09.2024\nClasses 7 weeks 23.09.2024 - 10.11.2024\nMid-Semester Break 1 week 11.11.2024 - 17.11.2024\nClasses 7 weeks 18.11.2024 - 05.01.2025\nRevision Week 1 week 06.01.2025 - 12.01.2025\nExaminations 2 weeks 13.01.2025 - 26.01.2025\nEnd-Semester Break 3 weeks 27.01.2025 - 16.02.2025\nFEBRUARY SEMESTER\nRegistration/Orientation 4 days 11.02.2025 - 14.02.2025\nClasses 6 weeks 17.02.2025 - 30.03.2025\nMid-Semester Break 1 week 31.03.2025 - 06.04.2025\nClasses 8 weeks 07.04.2025 - 01.06.2025\nRevision Week 1 week 02.06.2025 - 08.06.2025\nExaminations 2 weeks 09.06.2025 - 22.06.2025\nEnd-Semester Break 14 weeks 23.06.2025 - 28.09.2025\nJULY SEMESTER (Short Semester)\nClasses 7 weeks 07.07.2025 - 24.08.2025\nRevision Week 1 week 25.08.2025 - 31.08.2025\nExaminations 1 week 01.09.2025 - 07.09.2025\nEnd-Semester Break 3 weeks 08.09.2025 - 28.09.2025"
                },
                {
                "text": "input: ACADEMIC CALENDAR FOR FOUNDATION STUDIES"
                },
                {
                "text": "output: ACADEMIC CALENDAR FOR FOUNDATION STUDIES\n SESSION 2023-2024\nSEMESTER ONE\nRegistration & Orientation 4 days 20.06.23 - 23.06.23\nClasses 7 weeks 26.06.23 - 13.08.23\nMid-Semester Break 1 week 14.08.23 - 20.08.23\nClasses 7 weeks 21.08.23 - 08.10.23\nRevision Week 1 week 09.10.23 - 15.10.23\nExaminations 2 weeks 16.10.23 - 29.10.23\nEnd-Semester Break 3 weeks 30.10.23 - 19.11.23\nSEMESTER TWO\nRegistration & Orientation 4 days 14.11.23 - 17.11.23\nClasses 7 weeks 20.11.23 - 07.01.24\nMid-Semester Break 1 week 08.01.24 - 14.01.24\nClasses 7 weeks 15.01.24 - 03.03.24\nRevision Week 1 week 04.03.24 - 10.03.24\nExaminations 2 weeks 11.03.24 - 24.03.24\nEnd-Semester Break 3 weeks 25.03.24 - 14.04.24\nSEMESTER THREE\nClasses 7 weeks 15.04.24 - 02.06.24\nRevision Week 1 week 03.06.24 - 09.06.24\nExaminations 1 week 10.06.24 - 16.06.24\nEnd of Study Programme"
                },
                {
                "text": "input: Bachelor of Civil Engineering"
                },
                {
                "text": "output: The Bachelor of Civil Engineering (Hons) at UTS provides a comprehensive curriculum covering disciplines like structures, materials, hydraulics, geotechnical, highway, and surveying. Accredited by MQA and EAC, it aims to produce graduates equipped with strong technical skills, ethical values, and effective communication abilities. The program emphasizes problem-solving, teamwork, and lifelong learning, preparing graduates for diverse engineering roles. With experienced faculty and modern facilities, including internships for practical experience, graduates have a 100% employability rate, eligible for professional engineering registration."
                },
                {
                "text": "input: The Bachelor of Accountancy"
                },
                {
                "text": "output: The Bachelor of Accountancy (Honours) program at UTS is a three-year professional degree aligned with MQA and MIA standards. It equips students with accounting concepts, management understanding, leadership skills, and analytical abilities for decision-making. Accredited by MQA, CTIM, ACCA, and CPA Australia, the program integrates finance, management, economics, and entrepreneurial skills. Graduates develop competencies in accounting principles, financial interpretation, entrepreneurship, effective communication, critical thinking, and ethical professionalism. Entry requirements include STPM, A-levels, UEC, Matriculation/Pre-U/Foundation, or equivalent qualifications. Full-time study lasts three years. Tuition fees are available, and study loans from PTPTN are accessible for local/Malaysian students. For inquiries, contact the Marketing Office at (+6) 084-367300 or email enquiry@uts.edu.my."
                },
                {
                "text": "input: The Bachelor of Science (Hons) in Architecture"
                },
                {
                "text": "output: The Bachelor of Science (Hons) in Architecture at UTS is a three-year program aimed at producing creative and innovative architects. Accredited by LAM Part I and recognized by MQA, it integrates theoretical understanding with practical skills and includes a compulsory internship. The program'\''s vision is to be a global technical university, while its mission is to provide world-class education in science and technology. Graduates are expected to have a strong architectural background and ethical values. The curriculum covers design, building technology, environmental science, history, and theory of architecture. Elective subjects include Computer Aided Design, Green Architecture, and Environmental Psychology. Entry requirements include STPM/A-Level, UEC, Matriculation/Pre-U/Foundation, or equivalent qualifications with credits in Mathematics. Career prospects include roles like Assistant Architect, Design Consultant, Interior Designer, and Graphic Illustrator."
                },
                {
                "text": "input: UTS'\''s Bachelor of Arts (Hons) Interior Design"
                },
                {
                "text": "output: UTS'\''s Bachelor of Arts (Hons) Interior Design is the first-degree program of its kind in Sarawak and Sabah. It aims to produce Registered Interior Designers recognized by LAM and MIID. The curriculum focuses on research and problem-based learning, integrating theoretical knowledge with practical skills. Students engage in design studios, lectures, workshops, and site visits. The program covers design principles, building technology, furniture design, and more. Elective courses include Architectural & Interior Graphic and Green Architecture. Entry requirements include foundation or diploma programs, STPM/A-Level, UEC, or equivalent qualifications, along with a portfolio review. Career options include Interior Designer, Product Designer, Graphic Designer, and more."
                },
                {
                "text": "input: UTS'\''s Bachelor of Business Administration (BBA) program"
                },
                {
                "text": "output: UTS'\''s Bachelor of Business Administration (BBA) program from the School of Business and Management (SBM) equips students with essential knowledge in business administration, leadership, and analytical skills. With full accreditation from MQA, the program focuses on multidisciplinary practices, leadership, and effective communication. Graduates can evaluate business theories, communicate ideas effectively, apply critical thinking for decision-making, demonstrate entrepreneurial skills, exhibit leadership and teamwork, and apply lifelong learning principles. The program spans three years with 120 credits. Entry requirements include STPM/A-Level, UEC, Matriculation/Pre-U/Foundation, or relevant diplomas. Credit transfers up to 30% are possible for diploma holders. Tuition fees are subject to change, and study loans are available for local/Malaysian students. For more information, contact the Marketing Office."
                },
                {
                "text": user_message
                },
                {
                "text": "output: "
                }
            ]
        }
        ]
    }
    
    try:
        response = requests.post(ai_service_endpoint, json=test)
        response.raise_for_status()  
        return {'response': response.json()}
    except requests.HTTPError as e:
        logging.error(f"HTTP error: {str(e)}")
        return {'error': 'Failed to get AI response'}, e.response.status_code
    except requests.RequestException as e:
        logging.error(f"Request error: {str(e)}")
        return {'error': 'Failed to get AI response'}, 500
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return {'error': 'Internal server error'}, 500

@app.route('/chat', methods=['POST'])
def chat():
    if request.method == 'POST':
        try:
            user_message = request.json.get('input')
            if not user_message:
                logging.error('Invalid input: No message provided')
                return jsonify({'error': 'Invalid input', 'status_code': 400}), 400

            logging.info(f"Received message: {user_message}")
            ai_service_response = get_ai_service_response(user_message)
            
            if 'error' in ai_service_response:
                logging.error(f"AI service response error: {ai_service_response['error']}")
                return jsonify({'error': ai_service_response['error'], 'status_code': 500}), 500
            
            logging.info(f"AI response: {ai_service_response}")

            # Log response content
            logging.info(f"AI response content: {ai_service_response['response']}")

            return jsonify({'response': ai_service_response['response'], 'status_code': 200})
        except Exception as e:
            logging.error(f"Exception occurred: {str(e)}")
            return jsonify({'error': 'Failed to process the request', 'status_code': 500}), 500
    
    return jsonify({'error': 'Invalid request method', 'status_code': 400}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)