from flask import Flask,jsonify,request
from flask_cors import CORS
from os import environ,path, getcwd
from config import db,SECRET_KEY
from dotenv import load_dotenv
from models.user import User
from models.personalDetails import PersonalDetails
from models.projects import Projects
from models.experiences import Experiences
from models.education import Education
from models.certificates import Certificates
from models.skills import Skills


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URI")
    app.config["SQLALCHEMY_TRACK_MODOFICATIONS"] = False
    app.config["SQLALCHEMY_ECHO"] = False
    app.secret_key = SECRET_KEY
    db.init_app(app)
    print("DB Initialized Successfully")
    with app.app_context():
        # db.drop_all()
        #create end points
        # -sign up user
        # -add personal details
        # -add projects
        # -add experiences
        # -add education
        # -add certificates
        # -add skills
        @app.route('/sign_up', methods=['POST'])
        def sign_up():
            # id = request.form.to_dict(flat=True)  
            data = request.form.to_dict(flat=True)
            new_user = User(
                username=data["username"],
            )
            db.session.add(new_user)
            db.session.commit()
            return "User added successfully"

          
        @app.route('/add_personal_details', methods=['POST'])
        def add_personal_details():
            if request.method == 'POST':
                username = request.args.get('username')
                user = User.query.filter_by(username=username).first()
                """
                {
                "name": "",
                "email": "",
                "phone": "",
                "address": "",
                "linkedin_link": ""
            }
            """

                personal_details = request.get_json()
                new_personal_details = PersonalDetails(
                    name=personal_details["name"],
                    email=personal_details["email"],
                    phone=personal_details["phone"],
                    address=personal_details["address"],
                    linkedin_link=personal_details["linkedin_link"],
                    user_id=user.id
                )
            db.session.add(new_personal_details)
            db.session.commit()
            return "User added successfully"




        @app.route('/add_projects', methods=['POST'])
        def add_projects():
            if request.method == 'POST':
                username = request.args.get('username')
                user = User.query.filter_by(username=username).first()
                project_details = request.get_json()

                for  data in project_details["data"]:
                    new_project_details = Projects(
                        
                            name = data["name"],
                            desc = data["description"],
                            start_date = data["start_date"],
                            end_date = data["end_date"],
                            user_id = user.id
                
                    )

                
                    db.session.add(new_project_details)
                    db.session.commit()   
            return "project added successfully"




        @app.route('/add_experience', methods=['POST'])
        def add_experience():
          
            if request.method == 'POST':
                username = request.args.get('username')
                user = User.query.filter_by(username=username).first()
                experience_details = request.get_json()

                for data in experience_details["data"]:
                    new_experience_details = Experiences(
                        
                        company_name = data["company_name"],
                        role = data["role"],
                        role_desc = data["description"],
                        start_date = data["start_date"],
                        end_date = data["end_date"],
                        user_id = user.id
                
                )

                
                    db.session.add(new_experience_details)
                    db.session.commit()   
            return "experiences added successfully"



        @app.route('/add_education', methods=['POST'])
        def add_education():
            if request.method == 'POST':
                username = request.args.get('username')
                user = User.query.filter_by(username=username).first()
                education_details = request.get_json()

                for data in education_details["data"]:
                    new_education_details = Education(
                        
                        school_name = data["company_name"],
                        degree_name = data["company_name"],
                        start_date = data["start_date"],
                        end_date = data["end_date"],
                        user_id = user.id
                
                )

                
                    db.session.add(new_education_details)
                    db.session.commit()   
            return "education added successfully"




        @app.route('/add_certificate', methods=['POST'])
        def add_certificate():
            if request.method == 'POST':
                username = request.args.get('username')
                user = User.query.filter_by(username=username).first()
                certificate_details = request.get_json()

                for data in certificate_details["data"]:
                    new_certificate_details = Certificates(
                        
                        title = data["title"],
                        start_date = data["start_date"],
                        end_date = data["end_date"],
                        user_id = user.id
                
                )
                
                    db.session.add(new_certificate_details)
                    db.session.commit()
                    
            return "certificates added successfully"



        @app.route('/add_skill', methods=['POST'])
        def add_skill():
            if request.method == 'POST':
                username = request.args.get('username')
                user = User.query.filter_by(username=username).first()
                skill_details = request.get_json()

                for data in skill_details["data"]:
                    new_skill_details = Skills(
                        
                        name = data["name"],
                        confidence = data["confidence"],
                        user_id = user.id
                
                )
                
                    db.session.add(new_skill_details)
                    db.session.commit()
                
            return "skills added successfully"




        @app.route('/get_resume', methods=['GET'])
        def get_resume():
            username = request.args.get('username')
            user = User.query.filter_by(username=username).first()
            personal_details = PersonalDetails.query.filter_by(user_id=user.id).first()
            # experiences = Experience.query.filter_by(user_id=user.id).all()
            # education = Education.query.filter_by(user_id=user.id).all()
            # skills = Skill.query.filter_by(user_id=user.id).all()
            # certificates = Certificate.query.filter_by(user_id=user.id).all()
            projects = Projects.query.filter_by(user_id=user.id).all()

        
            experiences_data = []
            education_data = []
            skills_data = []
            certificates_data = []
            projects_data = []

            resume_data = {
                "name": personal_details.name,
                "email": personal_details.email,
                "phone": personal_details.phone,
                "address": personal_details.address,
                "linkedin_link": personal_details.linkedin_link
            }

            #add experience
            # for experience in experiences:
            #     experiences_data.append({
            #         "company_name": experience.company_name,
            #         "role": experience.role,
            #         "role_description": experience.role_description,
            #         "start_date": experience.start_date,
            #         "end_date": experience.end_date
            #     })
            # resume_data["experiences"] = experience_data


            # #add education
            # for education in education:
            #     education_data.append({
            #         "school_name": education.school_name,
            #         "degree_name": education.degree_name,
            #         "start_date": education.start_date,
            #         "end_date": education.end_date
            #     })
            # resume_data["education_data"] = education_data


            #add skills
            # for skill in skills:
            #     skills_data.append({
            #         "name": skill.name,
            #         "confidence": skill.confidence
            #     })
            # resume_data["skills"] = skills_data

            #add certificates
            # for certificate in certificates:
            #     certificates_data.append({
            #         "title": certificate.title,
            #         "start_date": certificate.start_date,
            #         "end_date": certificate.end_date
            #     })
            # resume_data["certificates"] = certificates_data

            #add projects
            for project in projects:
                projects_data.append({
                    "name": project.name,
                    "description": project.desc,
                    "start_date": project.start_date,
                    "end_date": project.end_date
                })

            resume_data["projects"] = projects_data

            return resume_data


        db.create_all()
        db.session.commit()
        return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

