import gradio as gr

def generate_cv_and_skills(name, age, job_title, skills_input, cv_input, regenerate):
    if regenerate:
        cv_text = (
            f"{name} is a dedicated and results-driven {job_title} aged {age}, "
            "demonstrating exceptional skills in problem-solving, innovation, and teamwork. "
            "Possesses strong communication abilities, adaptability to dynamic work environments, "
            "and a commitment to continuous learning and professional development. "
            "Experienced in delivering high-quality projects and contributing positively to organizational goals."
        )
        
        skills_lookup = {
            # التقنية
            "software developer": [
                "Python", "Java", "C++", "JavaScript", "TypeScript", "Dart", "Flutter", "React", "Angular",
                "Node.js", "Git", "Docker", "Kubernetes", "REST APIs", "SQL", "NoSQL", "Unit Testing",
                "Agile Methodologies", "CI/CD", "Problem Solving", "Team Collaboration"
            ],
            "data scientist": [
                "Python", "R", "Machine Learning", "Deep Learning", "Statistics", "Data Visualization",
                "SQL", "TensorFlow", "PyTorch", "Pandas", "NumPy", "Big Data", "Data Cleaning", "Model Deployment",
                "Data Mining", "Critical Thinking"
            ],
            "graphic designer": [
                "Adobe Photoshop", "Adobe Illustrator", "InDesign", "Creativity", "UI/UX Design", 
                "Typography", "Branding", "Sketch", "Figma", "Adobe XD", "Color Theory", "Logo Design",
                "Attention to Detail", "Time Management"
            ],
            "digital marketer": [
                "SEO", "Google Analytics", "Google Ads", "Facebook Ads", "Content Creation", "Email Marketing",
                "Social Media Management", "Copywriting", "Keyword Research", "Campaign Management",
                "Data Analysis", "Marketing Strategy", "Creativity"
            ],
            "teacher": [
                "Curriculum Development", "Classroom Management", "Public Speaking", "Lesson Planning",
                "Student Assessment", "Patience", "Communication", "Adaptability", "Teamwork",
                "Educational Technology"
            ],
            "project manager": [
                "Project Planning", "Risk Management", "Agile Methodologies", "Scrum", "Budget Management",
                "Team Leadership", "Communication", "Stakeholder Management", "Scheduling", "Problem Solving"
            ],

            # الصحة والطب
            "doctor": [
                "Patient Care", "Diagnosis", "Treatment Planning", "Medical Research", "Clinical Skills",
                "Communication", "Emergency Response", "Pharmacology", "Record Keeping", "Teamwork"
            ],
            "nurse": [
                "Patient Monitoring", "Medication Administration", "Patient Education", "Record Keeping",
                "Communication", "Compassion", "Emergency Response", "Vital Signs Assessment"
            ],
            "pharmacist": [
                "Medication Dispensing", "Pharmacology", "Patient Counseling", "Inventory Management",
                "Attention to Detail", "Regulatory Compliance"
            ],
            "physical therapist": [
                "Patient Assessment", "Rehabilitation", "Exercise Therapy", "Patient Education",
                "Communication", "Empathy"
            ],
            "medical assistant": [
                "Clinical Support", "Patient Scheduling", "Record Keeping", "Vital Signs Monitoring",
                "Communication", "Basic Medical Procedures"
            ],
            "dentist": [
                "Oral Health Care", "Diagnosis", "Treatment Planning", "Patient Education", "Surgical Skills"
            ],
            "psychologist": [
                "Patient Assessment", "Therapy", "Counseling", "Research", "Communication", "Empathy"
            ],

            # الهندسة
            "civil engineer": [
                "AutoCAD", "Project Management", "Structural Analysis", "Surveying", "Construction Management",
                "Problem Solving", "Teamwork"
            ],
            "mechanical engineer": [
                "CAD Software", "Thermodynamics", "Materials Science", "Manufacturing Processes",
                "Problem Solving", "Team Collaboration"
            ],
            "electrical engineer": [
                "Circuit Design", "MATLAB", "Power Systems", "Control Systems", "Troubleshooting", "Teamwork"
            ],
            "chemical engineer": [
                "Process Engineering", "Safety Procedures", "Data Analysis", "Laboratory Skills", "Teamwork"
            ],
            "architect": [
                "Design Software", "Project Planning", "Creative Thinking", "Construction Knowledge", "Communication"
            ],

            # الأعمال والإدارة
            "accountant": [
                "Financial Reporting", "QuickBooks", "Excel", "Budgeting", "Tax Preparation", "Attention to Detail"
            ],
            "business analyst": [
                "Data Analysis", "Requirements Gathering", "Stakeholder Communication", "Problem Solving",
                "Process Improvement"
            ],
            "human resources manager": [
                "Recruitment", "Employee Relations", "Performance Management", "Conflict Resolution", "Communication"
            ],
            "sales manager": [
                "Sales Strategy", "Negotiation", "Customer Relationship Management", "Team Leadership",
                "Communication", "Target Achievement"
            ],
            "customer service representative": [
                "Communication", "Problem Solving", "CRM Software", "Patience", "Conflict Resolution"
            ],

            # التعليم والتدريب
            "university professor": [
                "Research", "Teaching", "Curriculum Development", "Public Speaking", "Academic Writing"
            ],
            "trainer": [
                "Training Delivery", "Curriculum Design", "Communication", "Assessment", "Motivation"
            ],

            # قائمة عامة (fallback)
            "default": [
                "Communication", "Teamwork", "Problem Solving", "Adaptability", "Leadership",
                "Time Management", "Critical Thinking", "Creativity", "Organizational Skills", "Customer Service"
            ],
        }
        
        # جلب المهارات أو استخدام الافتراضي
        suggested_skills = skills_lookup.get(job_title.lower(), skills_lookup["default"])
        skills_text = ", ".join(suggested_skills)

        return cv_text, skills_text

    return cv_input, skills_input


with gr.Blocks() as demo:
    gr.Markdown("### AI Resume & Skills Assistant with Extensive Job Titles")
    with gr.Row():
        name = gr.Textbox(label="Full Name")
        age = gr.Textbox(label="Age")
        job_title = gr.Textbox(label="Job Title")
    skills = gr.Textbox(label="Skills (comma separated)", lines=5)
    cv = gr.Textbox(label="Your CV (editable)", lines=10)
    regenerate_btn = gr.Button("Regenerate CV and Skills")

    regenerate_btn.click(
        fn=generate_cv_and_skills,
        inputs=[name, age, job_title, skills, cv, gr.State(True)],
        outputs=[cv, skills]
    )

    name.change(
        fn=generate_cv_and_skills,
        inputs=[name, age, job_title, skills, cv, gr.State(False)],
        outputs=[cv, skills]
    )
    age.change(
        fn=generate_cv_and_skills,
        inputs=[name, age, job_title, skills, cv, gr.State(False)],
        outputs=[cv, skills]
    )
    job_title.change(
        fn=generate_cv_and_skills,
        inputs=[name, age, job_title, skills, cv, gr.State(False)],
        outputs=[cv, skills]
    )

demo.launch()