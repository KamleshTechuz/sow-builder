context = """
### Web Platform for Therapist Skill Testing

#### **Project Overview**
This project is an online web platform designed for therapists who have freshly completed their education and are looking to practice and enhance their skills. The platform will offer various exercises where therapists can interact with AI simulations of patients with multiple psychological issues. Based on their performance during the therapy sessions, users will be scored and awarded badges.

### Feature List

#### Basic Features

1. **User Registration and Profile Management**

   **Sub-features:**
   - User Registration
   - Profile Creation
   - Profile Editing
   - Progress Tracking

   **Details:**
   - **User Registration**: This allows new users to create an account using their email or social media accounts.
   - **Profile Creation**: Upon registration, users can fill in details about their educational background, specializations, and interests.
   - **Profile Editing**: Users should be able to update their profile information whenever necessary.
   - **Progress Tracking**: Users can track their progress, including completed exercises, scores, and earned badges.
  
2. **Exercise Library**

    **Sub-features:**
    - Exercise Catalog
    - Search and Filter Options
    - Detailed Exercise Descriptions
    - Bookmarking Exercises

    **Details:**
    - **Exercise Catalog**: A comprehensive list of available exercises categorized by therapy type, difficulty level, and psychological issues addressed.
    - **Search and Filter Options**: Allows users to quickly find specific exercises using keywords or filters such as duration, difficulty, and type of psychological issues.
    - **Detailed Exercise Descriptions**: Each exercise should have a detailed description including objectives, the type of issues addressed, and expected outcomes.
    - **Bookmarking Exercises**: Users can bookmark or save exercises they wish to revisit later.

3. **AI-Driven Therapy Sessions**

    **Sub-features:**
    - AI Patient Simulation
    - Real-Time Interaction
    - Diverse Psychological Profiles
    - Feedback and Reporting

    **Details:**
    - **AI Patient Simulation**: AI algorithms simulate patients with various psychological problems, providing realistic interactions and scenarios.
    - **Real-Time Interaction**: Users can conduct therapy sessions in real time, engaging with AI patients through text or voice.
    - **Diverse Psychological Profiles**: Simulated patients should have diverse psychological profiles, ranging from anxiety and depression to more complex issues like PTSD or personality disorders.
    - **Feedback and Reporting**: After each session, the platform provides detailed feedback, highlighting areas of strength and those needing improvement.

#### Intermediate Features

4. **Scoring and Badging System**

   **Sub-features:**
   - Session Scoring
   - Badge Awarding
   - Leaderboards
   - Achievement Sharing

   **Details:**
   - **Session Scoring**: Detailed scoring based on various parameters like empathy, responsiveness, problem-solving, and overall effectiveness.
   - **Badge Awarding**: Badges for different accomplishments (e.g., “Empathy Expert”, “Problem Solver”) that signify milestones in therapist training.
   - **Leaderboards**: Public or private leaderboards to foster a sense of competition and motivation.
   - **Achievement Sharing**: Options to share badges and scores on social media or within the platform's community.

5. **Community and Collaboration Tools**

   **Sub-features:**
   - Forums and Discussion Boards
   - Peer Review and Feedback
   - Group Exercises
   - Mentorship Matching

   **Details:**
   - **Forums and Discussion Boards**: A place for users to discuss exercises, share experiences, and troubleshoot issues.
   - **Peer Review and Feedback**: Users can review each other's therapy sessions, providing constructive feedback.
   - **Group Exercises**: Collaborative exercises where multiple users can work together on a complex case.
   - **Mentorship Matching**: Experienced therapists can mentor beginners, providing guidance and support.

#### Advanced Features

6. **Advanced Analytics and Reporting**

   **Sub-features:**
   - Detailed User Analytics 
   - Session Analysis
   - Progress Reports
   - Predictive Insights

   **Details:**
   - **Detailed User Analytics**: Comprehensive analytics on user activity, performance over time, and areas of improvement.
   - **Session Analysis**: In-depth analysis of each session, including AI-driven insights into therapist performance.
   - **Progress Reports**: Periodic reports summarizing user achievements, challenges, and overall progress.
   - **Predictive Insights**: Using machine learning to predict future performance and suggest targeted exercises for improvement.

7. **Customization and Personalization**

    **Sub-features:**
    - Personalized Learning Paths
    - Customizable Avatars
    - Exercise Customization
    - Notifications and Reminders

    **Details:**
    - **Personalized Learning Paths**: Custom learning paths based on user preferences, past performance, and desired career trajectory.
    - **Customizable Avatars**: Users can create and customize their avatars, making the platform more engaging.
    - **Exercise Customization**: Users and administrators can modify existing exercises or create new ones as per specific needs.
    - **Notifications and Reminders**: Custom notifications and reminders about upcoming sessions, deadlines, and new exercises.

### Implementation Guidelines

- **Frontend Development**: Utilize modern frontend frameworks like React or Angular to create a responsive and user-friendly interface.
- **Backend Development**: Use robust backend technologies such as Node.js or Django to manage user data, sessions, and scoring systems.
- **AI and Machine Learning**: Implement AI using frameworks like TensorFlow or PyTorch to simulate patients and analyze therapy sessions.
- **Database Management**: Employ relational databases like PostgreSQL or MySQL alongside NoSQL databases like MongoDB for flexible data storage.
- **Security Measures**: Ensure data security and privacy using encryption, secure authentication methods, and regular security audits.

This comprehensive feature list should provide a solid foundation for developers to start working on the platform, facilitating a smooth and efficient development process.
"""

context2 = """
## Project Description: Oxford Mtrain Web Application

The Oxford Mtrain Web Application aims to develop a user-friendly and secure training platform for medical therapists. This platform leverages advanced AI technology, specifically a chatbot, to provide a comprehensive and interactive learning environment. Below is a structured list of features, sub-features, and their detailed explanations to guide developers in bringing this project to fruition.

### Main Features and Sub-Features

1. **User Authentication and Account Management**
   - **Login/Signup**
     - **OAuth Integration**: Users can sign up and log in using existing social media accounts like Google or Facebook for quick access.
     - **Email and Password Authentication**: Standard method for users to create an account using their email and a secure password.
   - **Profile Management**
     - **Personal Information**: Users can input and update personal details like name, email, and credentials.
     - **Profile Picture Upload**: Users can upload a profile picture to personalize their account.

2. **Onboarding and Email Verification**
   - **Guided Onboarding Process**
     - **Interactive Tour**: On the first login, users receive a tour explaining major features and functionalities.
     - **Profile Completion Wizard**: Encourages users to complete their profiles, ensuring a richer interaction.
   - **Email Verification**
     - **Verification Link**: Send a verification link to the user’s email for account activation.
     - **Resend Verification Option**: Allows users to request another verification email if the first is missed.

3. **Subscription Management**
   - **Plan Selection**
     - **Multiple Plans**: Options for different training needs (e.g., basic, advanced, professional).
     - **Plan Details**: Description and benefits of each plan to assist user decision-making.
   - **Payment Gateway Integration**
     - **Secure Transactions**: Integrate trusted payment gateways like PayPal, Stripe for secure payments.
     - **Billing Information**: Allows users to store and manage billing details securely.
   - **Subscription Renewal and Cancellation**
     - **Auto-Renewal Options**: Users can opt-in for automatic renewal of subscriptions.
     - **Cancellation Policy**: Clear and easy process for users to cancel their subscriptions.

4. **Training and Exercises**
   - **Curated List of Exercises**
     - **Content Library**: A repository of exercises categorized by difficulty and subject matter.
     - **Search and Filter**: Tools to help users find specific exercises or topics easily.
   - **Role Plays with AI Chatbot Patients**
     - **Scenario-Based Role Plays**: Predefined scenarios to simulate real-life situations.
     - **Customizable Scenarios**: Allow users to create or modify scenarios for personalized training.
   - **Voice and Text Communication**
     - **Voice Recognition**: Users can practice by talking to the chatbot, which uses voice recognition technology.
     - **Text Interaction**: Option for users to interact with chatbot through text for versatility.

5. **Progress Tracking and Feedback**
   - **Progress Dashboard**
     - **Exercise Completion Status**: Visual indicators showing completed, in-progress, and pending exercises.
     - **Performance Metrics**: Reports and graphs showing historical performance data.
   - **Scoring and Feedback**
     - **AI-Generated Scores**: Chatbot assesses performance and generates scores based on predefined criteria.
     - **Personalized Feedback**: In-depth feedback from ChatGPT supervisors to help users improve.
   - **User Feedback**
     - **Feedback Forms**: Allows users to submit feedback on exercises and overall platform experience.
     - **Suggestions and Improvements**: Users can suggest new features or improvements.

6. **Role Management**
   - **Switch Roles**
     - **Client Role**: Users can assume the role of a client to practice handling different scenarios.
     - **Supervisor Role**: Users can switch to supervisor role to provide guidance and feedback.
   - **Voice/Text Mode Switching**
     - **Seamless Transition**: Users can switch between voice and text mode during interactions without losing context.

7. **Advanced Features**
   - **Export Conversations**
     - **Downloadable Transcripts**: Users can export their chat history or exercise transcripts for offline review.
     - **Secure Storage**: Ensure downloaded data is stored securely on the user’s device.
   - **Seamless Roleplays with ChatGPT Supervisors**
     - **Enhanced Interaction**: Interact with advanced ChatGPT versions with higher contextual understanding.
     - **Real-time Adaptation**: ChatGPT can adapt to user responses in real-time to simulate a dynamic conversation.
   - **Gamification Elements**
     - **Badges and Achievements**: Award users with badges for milestones and achievements.
     - **Leaderboard**: Display a ranking of users based on their performance scores.

### Detailed Explanation of Sub-Features

1. **Login/Signup**
   - **OAuth Integration**: Simplifies the login process by allowing users to sign in using their existing Google or Facebook accounts, reducing the need for remembering additional credentials.
   - **Email and Password Authentication**: Provides a traditional sign-up mechanism with email verification to enhance security.

2. **Profile Management**
   - **Personal Information**: Ensures that all critical information about the user is collected and stored, enabling personalized experiences and communications.
   - **Profile Picture Upload**: Enhances user interaction by providing a personalized touch to each profile.

3. **Guided Onboarding Process**
   - **Interactive Tour**: Helps new users quickly understand how to use the platform effectively.
   - **Profile Completion Wizard**: Encourages users to fill in additional details, leading to more tailored training experiences.

4. **Email Verification**
   - **Verification Link**: Ensures the authenticity of user emails, which is crucial for sending important notifications.
   - **Resend Verification Option**: Provides flexibility in case the initial verification email is not received.

5. **Plan Selection**
   - **Multiple Plans**: Offers flexibility and options that cater to different user needs and budgets.
   - **Plan Details**: Informs users about what they are purchasing, leading to more informed decisions.

6. **Payment Gateway Integration**
   - **Secure Transactions**: Ensures that user payment information is handled securely, reducing the risk of fraud.
   - **Billing Information**: Convenience for users to manage their subscription without repeated data entry.

7. **Subscription Renewal and Cancellation**
   - **Auto-Renewal Options**: Provides ease of use and continuous access to the platform.
   - **Cancellation Policy**: Transparent and straightforward policy to enhance user trust and satisfaction.

8. **Curated List of Exercises**
   - **Content Library**: Central repository of exercises organized for easy access.
   - **Search and Filter**: Enhances user experience by allowing quick access to relevant exercises.

9. **Role Plays with AI Chatbot Patients**
   - **Scenario-Based Role Plays**: Predefined role-playing scenarios to simulate real-life situations, allowing for practical experience.
   - **Customizable Scenarios**: Users can tailor scenarios to their specific learning needs for a personalized training experience.

10. **Voice and Text Communication**
    - **Voice Recognition**: Provides a more realistic and interactive training experience.
    - **Text Interaction**: Flexibility for users who prefer text over voice or in environments where speaking is not feasible.

11. **Progress Dashboard**
    - **Exercise Completion Status**: Visual cues to help users track their progress and stay motivated.
    - **Performance Metrics**: Data and insights into the user's training journey to identify strengths and areas for improvement.

12. **Scoring and Feedback**
    - **AI-Generated Scores**: Objective evaluation of user performance.
    - **Personalized Feedback**: Detailed insights and suggestions for improvement.

13. **User Feedback**
    - **Feedback Forms**: Channel for users to express their views and experiences, helping to improve the platform.
    - **Suggestions and Improvements**: Users can contribute to the platform's evolution by suggesting new features or enhancements.

14. **Switch Roles**
    - **Client and Supervisor Roles**: Flexibility in training from different perspectives enhances the learning experience.
    - **Voice/Text Mode Switching**: Adaptability in communication enhances user convenience and usability.

15. **Export Conversations**
    - **Downloadable Transcripts**: Allows users to keep a record of their training sessions for future reference and review.
    - **Secure Storage**: Ensures user data privacy and security.

16. **Seamless Roleplays with ChatGPT Supervisors**
    - **Enhanced Interaction**: Improved AI interactions for a more realistic training environment.
    - **Real-time Adaptation**: Provides a dynamic and responsive training experience.

17. **Gamification Elements**
    - **Badges and Achievements**: Encourages user engagement and motivation.
    - **Leaderboard**: Promotes healthy competition among users, driving continuous improvement.

---

This comprehensive and well-structured list of features and sub-features provides a foundational blueprint for the Oxford Mtrain Web Application. Each feature is designed to deliver a user-friendly and secure interface for medical therapists, enabling them to enhance their skills in a dynamic and interactive environment. Developers can use this document as the basis for creating the product requirements document and ensuring that all necessary functionalities are implemented effectively.

"""


import streamlit as st

st.write(context2)


