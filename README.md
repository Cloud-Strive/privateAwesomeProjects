Investor Matching Application Documentation

1. Overview
   This is a Flask-based web application that facilitates matching between investors and startups/research projects. It uses machine learning to predict potential matches based on user profiles and project descriptions. The application includes user authentication, profile management, and a matching algorithm.

2. Dependencies
   - Flask: Web framework
   - SQLAlchemy: ORM for database management
   - Flask-Login: User session management
   - Flask-WTF: Form handling and validation
   - Flask-Mail: Email functionality
   - scikit-learn: Machine learning library for matching algorithm
   - pandas: Data manipulation and analysis
   - numpy: Numerical computing
   - joblib: Model serialization

3. Main Components

   3.1 Database Models
   - User: Stores user authentication information
   - StartupProfile: Stores startup/entrepreneur profile information
   - InvestorProfile: Stores investor profile information

   3.2 Forms
   - LoginForm: User login
   - RegistrationForm: User registration
   - RequestResetForm: Password reset request
   - ResetPasswordForm: Password reset
   - StartupProfileForm: Startup profile creation/edit
   - InvestorProfileForm: Investor profile creation/edit

   3.3 Data Processing and Model Training
   - load_csv(): Loads CSV files with error handling
   - extract_combined_features(): Extracts and combines relevant features from datasets
   - handle_missing_values(): Fills in missing values in datasets
   - create_samples(): Creates positive and negative samples for model training
   - train_and_evaluate_model(): Trains and evaluates machine learning models
   - process_data_and_train_model(): Main function for data processing and model training

   3.4 User Authentication and Management
   - Registration with email verification
   - Login/Logout functionality
   - Password reset functionality

   3.5 Profile Management
   - Separate dashboards for startups and investors
   - Profile creation and viewing

   3.6 Matching Algorithm
   - Uses trained model to predict matches between investors and startups/projects

4. Routes
   - /: Home page
   - /about: About page
   - /login: User login
   - /register: User registration
   - /verify_email/<token>: Email verification
   - /reset_password: Password reset request
   - /reset_password/<token>: Password reset
   - /startup_profile: Startup profile creation/edit
   - /investor_profile: Investor profile creation/edit
   - /startup_dashboard: Startup user dashboard
   - /investor_dashboard: Investor user dashboard
   - /logout: User logout
   - /match: API endpoint for matching algorithm
   - /add_profile: API endpoint for adding new profiles to datasets

5. Key Functions

   5.1 process_data_and_train_model()
   - Loads and preprocesses datasets
   - Extracts and combines features
   - Performs feature selection
   - Trains and evaluates Gradient Boosting and Random Forest models
   - Selects the best performing model

   5.2 match()
   - Handles matching requests
   - Uses trained model to predict match scores between investor and target profiles

   5.3 add_profile()
   - Adds new profiles to the respective CSV datasets

6. Machine Learning Pipeline
   - TF-IDF vectorization for text data
   - Feature selection using VarianceThreshold and SelectKBest
   - Model training using GridSearchCV for hyperparameter tuning
   - Model evaluation using cross-validation and various metrics

7. Email Functionality
   - Email verification for new user registration
   - Password reset emails

8. Data Storage
   - User data stored in SQLite database
   - Profile data stored in CSV files

9. Security Features
   - Password hashing
   - Token-based email verification and password reset
   - Login required for accessing certain routes

10. Logging
    - Comprehensive logging for debugging and monitoring

11. Future Improvements
    - Implement more robust error handling
    - Add more advanced matching algorithms
    - Improve UI/UX with JavaScript and AJAX
    - Implement data visualization for matching results
    - Add more comprehensive user profile management
    - Implement real-time notifications for new matches

Note: This application handles sensitive user data and should be deployed with appropriate security measures. The current implementation uses hardcoded file paths and email credentials, which should be replaced with environment variables or a configuration file for production use.
