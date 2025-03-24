import streamlit as st
from PIL import Image

profile_pic = Image.open('portfolio_image.png')

st.set_page_config(page_title='Udhayaprasad s portfolio',layout='wide',page_icon='portfolio_image.png')
st.sidebar.header('Welcome to My Portfolio Website')
st.sidebar.image(profile_pic,caption='Udhayaprasad s')

option = st.sidebar.selectbox('Navigation Menu',options=['Home','Experience','Projects','Publications','Certifications',])
linkedin_url = "https://www.linkedin.com/in/udhayaprasad-s-9592bb272/"
google_url = 'https://scholar.google.com/citations?user=7UbB8JIAAAAJ&hl=en'

st.sidebar.markdown(f""" Connect With Me:                     
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?logo=linkedin)]({linkedin_url})  [![GoogleScholar](https://img.shields.io/badge/GoogleScholar-white?logo=GoogleScholar)]({google_url})
[![ResearchGate](https://img.shields.io/badge/ResearchGate-black?logo=ResearchGate)]({'https://www.researchgate.net/profile/Udhaya-Prasad-S'})
[![Github](https://img.shields.io/badge/Github-black?logo=Github)]({'https://github.com/UdhayaPrasad'})

""")

st.sidebar.divider()
st.sidebar.text('Made with ❤️ by Udhay')

def Experience():
     st.header('Experience:')  
     st.markdown("""- **[CODE ALPHA](https://github.com/UdhayaPrasad/CodeAlpha_Task)** - ***Machine Learning Intern*** - Dec 2024 - Jan 2025""")
     st.write(" I gained hands-on experience in developing predictive models and implementing algorithms while working with advanced frameworks like TensorFlow and scikit-learn I enhanced my programming skills and learned effective data preprocessing techniques, collaborating closely with professionals to tackle practical challenges. This experience allowed me to contribute to impactful projects and build a strong foundation for a career in machine learning.")
     st.divider()
     st.markdown(""" - **[BHARAT INTERN](https://github.com/UdhayaPrasad/Bharat_Intern_ML)** - ***Machine Learning Intern*** - May 2024 - Jun 2024""")
     st.write("Enhanced machine learning model accuracy by implementing advanced algorithms and feature engineering techniques.Performed exploratory data analysis to identify patterns, trends, and potential features for machine learning models.Studied new technologies to support machine learning applications.Transformed raw data to conform to assumptions of machine learning algorithm.")
     st.divider()
     st.markdown("""- **[CODE CASA](https://github.com/UdhayaPrasad/Code_Casa_Python_Task)** - ***Python Developer Intern*** - May 2024 - Jun 2024""")
     st.write("The Python Developer Internship at Code Casa provided me with a stimulating learning environment and valuable hands-on experience in Python programming and software development. and Build a Simple Attendance Tracker System")
     st.divider()
     st.markdown(""" 
                 - **Cognifyz Technologies** - ***Web Developer Intern*** - Dec 2023 - Jan 2024""")
     st.write("The web development internship at Cognifyz Technologies provided me with a solid foundation in web development technologies and frameworks, equipping me with the skills and knowledge necessary to build dynamic and engaging web application")
     st.divider()
     st.markdown(""" 
                 - **National Institute Of Technology Puducherry, Karaikal** - ***Search Engine Optimization (SEO)*** - Jul 2023 - Nov 2023 """)
     st.write("We Conducted A Competitive Analysis on Top NIRF Universities and International Universities , Comparing crucial SEO factors. mentored by Dr. Surendiran, Associate Professor Department of Computer Science and Engineering, and Dean Faculty Welfare at the National Institute of Technology Puducherry, Ajay Viswanathan CEO @ Superfect Solutions. which resulted in Conference paper")
     
     
     
    
def Home():
  col1,col2 = st.columns([1,10])
  with col1:
      st.image(profile_pic)
  with col2:
      st.header("Hello I'm Udhayaprasad s:wave:")
      st.markdown("""**Aspiring Software Engineer and Machine Learning & Data Science Enthusiast**""")
      resume = 'UDHAYAPRASAD_RESUME.pdf'
      with open(resume,'rb')as pdf_file:
          pdf_data = pdf_file.read()
      st.download_button(label='Download Resume',data=pdf_data,file_name='UDHAYAPRASAD_RESUME.pdf',mime='application')
  st.subheader('About Me')
 
  st.markdown(""" 
I am currently in the Pre-Final Year of my Computer Science and Engineering degree at National Institute of Technology Puducherry, where I specialize in Artificial Intelligence and Machine Learning. My main focus is to web and mobile applications which solve real life solutions using data science, machine learning and software development methodologies.

Throughout my studies, I have developed a solid understanding of numerous programming languages, such as C, C++, Java, Python, and Dart. This diverse background has provided me with a diverse set of skills, making it possible for me to apply theoretical study to the real world which includes mobile application development with Flutter, and web development with HTML, CSS, and JS. In addition, I have been utilizing essential data science packages like Pandas, NumPy, and scikit-learn to further my understanding of data analysis and modeling. Furthermore, I have developed my skills with data visualization tools such as Power BI and utilized them to discover valuable insights, which can be used to create advanced predictive models that are utilized for helping informed decision-making.

Fusing theoretical knowledge with hands-on experience, I strive to hone my skills while further grasping the evolving domains of AI, machine learning, and data science, with an unwavering resolve to employ these advancements in the service of significant and beneficial change.
""") 
  



def Projects():
    st.header('Projects')
    st.text("Here are some of my projects.")
    st.markdown(""" 
- **Personal Voice Assistant** - [Link](https://github.com/UdhayaPrasad/Projects/blob/main/Mona.py) :
                
Developed a Personal Voice Assistant capable of performing various tasks through voice command using Google API. Key
features include playing music from YouTube, performing Google searches, opening applications, and sending emails and
WhatsApp messages.
Tools & Technologies: Python, pyttsx3, speech recognition, smtplib
                
- **Analysis of Insulin Concentration Levels in Normal and Dexamethasone-Induced Hyperglycemic Rats**-'https://insulin-concentration-prediction.streamlit.app/' 

Implemented supervised machine learning algorithms to predict insulin levels in rats and developed a web UI using Streamlit.
Algorithms: Random Forest, KNN, Decision Tree, AdaBoost.
Tools & Technologies: Python, scikit-learn, Pandas, Matplotlib, Seaborn, NumPy, Streamlit - Link

- **CYBER ATTACK DETECTION IN AD HOC NETWORK USING ARTIFICIAL INTELLIGENCE-[Link]('https://github.com/UdhayaPrasad/Projects/blob/main/supervised.py'):**  

Developed an intrusion detection system using the NSL-KDD dataset. Preprocessed data, selected features, and handled class
imbalance with SMOTE. Evaluated models using accuracy, precision, recall, and F1-score.

Algorithms: Random Forest, KNN, Decision Tree, XGBoost, SVM, Logistic Regression.
                
Tools & Technologies: Python, scikit-learn, Pandas, Matplotlib, Seaborn, NumPy, SMOTE

- **ASSESSMENT OF WATER BODIES PREDICTION FROM COASTAL AREAS USING REMOTE SENSING AND ARTIFICIAL INTELLIGENCE(Ongoing)**
                
Estimating water quality in coastal water bodies is crucial for sustainable long-term usage of water resources. Traditional techniques for assessing water quality may pose challenges such as high costs, more processing times, and the need for constant human intervention. To address these issues, the integration of satellite-based remote sensing imagery to get the data and apply it to various machine learning models. 
""")

def Publications():
    st.header('Publications')
    st.write("These are my publications.")
    st.markdown("""
    - **A Comparative Analysis of Top NIRF-Ranked Universities and International Universities Using Search
Engine Optimization Tools and Techniques (Springer Nature) (2024)** - [Link](https://link.springer.com/chapter/10.1007/978-981-97-3242-5_31):

- **A Comparative Analysis of Strength Prediction Using ANN and Ensemble Machine Learning Technique (2024)
(Scopus Indexed)(Accepted)**

- **Analysis of Insulin Concentration Levels in Normal and Dexamethasone-Induced Hyperglycemic Rats using
Machine Learning Approaches (Springer Nature) (2025) (Under Process)** 

- **Artificial Intelligence Based Techinques For Intrusion Detection In Wireless Ad hoc Network (IEEE) (2025) (Under
Process)**:
- **Assessment of Water Bodies Prediction from Coastal Areas Using Satellite Images and Artificial Intelligence (IEEE) (2025) (Under Process)**
    
    """)
def Certifications():
    st.header('Certifications:')
    st.markdown('*Power Bi*')
    st.image('power_bi.jpeg')
    st.markdown('*C & C++*')
    st.image('c.jpeg')
    st.markdown('*Basics of Python Programming:*')
    st.image('python_certificate_page-0001 - Copy.jpg')
    st.markdown('*Python for Data Analytics:*')
    st.image('python_data_analytics_page-0001.jpg')
    st.markdown("*Certificate for Developing a Web Interface for Conference ICET-2O25*:")
    st.image('image.png')
    
    


if option =='Experience':
    Experience()
elif option == 'Home':
    Home()
elif option == 'Projects':
    Projects()

elif option == 'Publications':
    Publications()
elif option =='Certifications':
    Certifications()
