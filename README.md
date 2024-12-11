# Workout Tracker

Workout tracker is a application where users can create and share workouts with eachother.

there is a library of oer 100+ exercises and exercise guides.

users can save eachothers workouts and rate and review them. 

# Rationale

## Target Audiences

This website is designed for fitness enthusiasts, personal trainers, and anyone looking to improve their physical fitness.

- **Users**: Can create and share workouts, track their progress, save workouts they find inspiring, and leave reviews for others' workouts.
- **Fitness Enthusiasts**: Gain access to a large repository of exercises with detailed instructions, images, and information on muscle groups and equipment.
- **Supporters**: Can donate to the platform to support its development and earn a custom username tag that highlights their contribution to the community.

## Introduction and Background

To understand this application, it’s essential to recognize the increasing demand for accessible, customizable fitness platforms that cater to diverse user needs. 

### Key Features of the Platform:

1. **Workout Creation and Sharing**  
   Users can design personalized workout plans, share them with the community, and browse through published workouts to find inspiration or guidance.

2. **Exercise Repository**  
   The website hosts hundreds of exercises with comprehensive details, including:
   - Step-by-step instructions.
   - Images or videos illustrating proper form.
   - Equipment needed for each exercise.
   - Primary and secondary muscles targeted.

3. **User Engagement and Reviews**  
   Workouts are open for reviews, enabling users to rate and provide feedback on workouts they've tried. This fosters a community-driven approach to fitness improvement.

4. **Progress Tracking**  
   Users can save workouts to their profiles and track their performance, making it easier to monitor progress over time.

5. **Donation System with Custom Username Tags**  
   Users can support the platform by donating. In return, they receive a custom username tag displayed across the site, signifying their support to others.

---

## Problems Addressed by the Application

Traditional fitness solutions often lack customization, accessibility, and community engagement. This application addresses several pain points for its target audience:

1. **Difficulty Accessing Reliable Fitness Information**  
   - The exercise library ensures users have accurate, detailed information on how to perform exercises safely and effectively.

2. **Limited Workout Customization Options**  
   - Users can create and publish their own workouts, offering unmatched flexibility for personalized fitness plans.

3. **Lack of Community and Motivation**  
   - The ability to review, rate, and save workouts fosters community engagement, encouraging users to stay motivated and connected.

4. **Tracking Progress**  
   - Users can save and revisit workouts they’ve completed, tracking their progress and maintaining consistency.

---

## How This Application Solves These Issues

1. **Comprehensive and User-Friendly Interface**  
   - The platform is designed to be intuitive and accessible, enabling users of all experience levels to navigate, create, and track workouts easily.

2. **Rich Database of Exercises**  
   - The extensive library of exercises ensures users always have new ideas and resources to enhance their fitness journey.

3. **Engagement Through Community Feedback**  
   - By allowing users to rate and review workouts, the application leverages community input to improve the quality and variety of content.

4. **Custom Features for Donors**  
   - Donations unlock unique username tags, creating a sense of exclusivity and recognition for supporters.

---

## The Data

The main data stored by this application includes:

- **Users**: Accounts to track activity, saved workouts, and donation status.
- **Workouts**: Details on the workout plans created by users, including ratings and reviews from others.
- **Exercises**: A comprehensive database of exercises with descriptions, images, equipment requirements, and targeted muscles.
- **Donations**: Records of user contributions and associated custom tags.

For more information on the database structure, see the [Database Schema](#database-schema).

---

## Project Scope and Limitations

This project provides a robust platform for fitness enthusiasts to create, share, and track workouts while fostering a supportive community. However, the following limitations are noted:

- **Scalability**: As the user base grows, querying large datasets for workouts, exercises, and user activity may require optimization.
- **Feature Requests**: Additional functionality, such as integrating wearables or advanced analytics, is not yet implemented.

---

## Future Versions

Planned future enhancements include:

1. **Advanced Analytics**  
   - Offer users insights into their progress, such as workout frequency and performance trends.

2. **Video Demonstrations**  
   - Include video guides for exercises alongside existing images and instructions.

3. **Gamification**  
   - Add badges or rewards for milestones achieved, such as completing a certain number of workouts or receiving positive reviews.

4. **Integration with Wearables**  
   - Enable users to sync fitness trackers and monitor heart rate, calories burned, and more.

5. **Mobile App Development**  
   - Expand the platform to include a mobile application for greater accessibility and convenience.

---

## User Experience (UX)

### User Stories

#### Website Owner Goals
1. As a website owner, I want to provide a platform where users can easily find, create, and track exercises and workouts.
2. As a website owner, I want to allow users to save and manage personalized workout plans.
3. As a website owner, I want to offer a seamless donation process with visible recognition for contributors.
4. As a website owner, I want to use Stripe for secure and efficient payment processing.
5. As a website owner, I want to maintain a user-friendly interface to ensure easy navigation and a positive user experience.
6. As a website owner, I want to encourage user engagement by enabling features like workout tracking and reviews.

#### First-Time User Goals
1. As a first-time user, I want to quickly understand the purpose of the website and its features on the home page.
2. As a first-time user, I want to easily navigate to the exercises section and explore exercises by filtering body parts.
3. As a first-time user, I want to view detailed instructions for exercises, including the required equipment and targeted muscles.
4. As a first-time user, I want to explore existing workouts and understand how they are structured.
5. As a first-time user, I want to easily access the donation page and understand the benefits of contributing.
6. As a first-time user, I want the website to be intuitive and visually appealing so I can easily find what I’m looking for.

#### Returning User Goals
1. As a returning user, I want to quickly access my saved workouts and track their progress.
2. As a returning user, I want to be able to review and modify workouts I’ve created.
3. As a returning user, I want to explore new exercises and workouts added to the platform since my last visit.
4. As a returning user, I want to leave reviews or feedback on workouts I’ve tried.
5. As a returning user, I want to manage my profile details, including my donation recognition status.

#### Frequent User Goals
1. As a frequent user, I want to efficiently track my workout progress by selecting days and weeks in the workout plan.
2. As a frequent user, I want detailed information about sets, reps, and execution for each exercise in my plan.
3. As a frequent user, I want to quickly create new workouts or edit existing ones to adapt to my fitness goals.
4. As a frequent user, I want to easily access and filter exercises by body parts or other criteria to keep my routines diverse.
5. As a frequent user, I want the website to provide a smooth and efficient experience to minimize the time spent navigating.



# Design 

## Imagery

The UI was given great consideration as it needed to be simple to give first time users quick and easy ways to navigate and figure out the exercises and workouts. 

the images used where diagrams from a website called [Simply Fitness](https://www.simplyfitness.com/) with the consent of the website owner and modified to fit the theme of the website. 



### Color Scheme 

The color scheme used was that of the Bootstrap3 for all button functions. 

the main colors used on the site are 

Success (Green): #5cb85c
Info (Blue): #5bc0de
Warning (Orange): #f0ad4e
Danger (Red): #d9534f
White
Black

![colors](/readme-images/read-me/Screenshot%202024-12-11%20163456.png)

### Layout 

The Website has 5 main Pages:

1. The Home page
   - this page quickly states what the user can do on the website and its main purpose 

2. The Exercises Home page
   - this page has different images of body parts that the user can use to filter through the large list of exercises. or naviagte to all exercises

   - 2.1 The Exercises Page. 
      - this displays all the exercises 

   - 2.2 The Exercises details Page.
      - this displays the exercise image, title and details on how to prefroe the exercise, what eqiptment is needed and what muscles are used.

3. The Workouts Home page 
   - this page shows all the different categories workouts can fall into and allows the user to filter by them 

   - 3.1 The Workouts page
      - This page displays all/filtered workouts 

   - 3.2 The Workouts Details page 
      - This page displays the workouts name an overview of the workout plan, reviews of the workout 
      - this page also allows users to save the workout to there probile to track it 
      - if the user is the owner they can edit the workout from here 

   - 3.3 The Create workout page 
      - this allows users to create there own workouts 

   - 3.4 Edit Workout page 
      - this allows users that have created a specific workout to edit that workout 

   - 3.5 Track workout 
      - This page lets the user select what day and week they are on and gives a carousel of what exercise is in that day or week.
      - they can access infomation about the sets and reps or the details on how to prefore the exercise. 

4. Profile page 
   - This page is where a users Saved workouts and created workouts are. 
   they can track the workouts from here or edit/ delete the workouts they have created.

5. The Donation Page
   - this page allows the user to select one of the classes of donations 
   - donation classes come with tags for the users that can be seen by other users, changing there name to the color of the class of the donation 

   - 5.1 Checkout page 
      - this page uses stripe for checkouts and allows the user to pay 
      - orders are created and the user profile is updated



## Wireframes

### Workouts Wireframes
<details>

 <summary>Desktop Wireframe</summary>

![Desktop Wireframe](/readme-images/read-me/workouts-wireframe.png)

 </details>

 <details>
    <summary>Mobile Wireframe</summary>

![Mobile Wireframe](/readme-images/read-me/workouts-mobile-wireframe.png)

 </details>

### Exercises Wireframes

<details>

 <summary>Desktop Wireframe</summary>

![Desktop Wireframe](/readme-images/read-me/exercises-wireframe.png)

 </details>

 <details>
    <summary>Mobile Wireframe</summary>

![Mobile Wireframe](/readme-images/read-me/exercises-mobile-wireframe.png)

 </details>

### Profile Wireframes

<details>

 <summary>Desktop Wireframe</summary>

![Desktop Wireframe](/readme-images/read-me/profile-wireframe.png)

 </details>

 <details>
    <summary>Mobile Wireframe</summary>

![Mobile Wireframe](/readme-images/read-me/profile-mobile-wireframe.png)

 </details>

### Changes since first designing the wire frames:

#### Home Pages 

I had orginally planned to for the workouts and exercises to just display when naviagted too but since adding filters and categories it made more sense to have a home page for each section. 



`Workouts` home page displays Levels, Sports and Fitnesses that would help a user find what specific workout they are looking for. 

---

`Exercises` home page displays the bodyparts with images to help the user find what specific exercise they want to use to target a specfic body part



#### Index

As the website has many different functions i decided to create the opening page explain some of the functionality. 

it explains to the user that they can Create workouts. Explore other users workouts. or search through the exercises to get detailed explanations on how to prefore the exercises


#### Donate

The section for donations was added instead of a subscription model as the business model did not make sense to implement with this website as there are applications that do similar things and the main draw of the website is the community element of it. therefore a free model is better to drive user engagement. 

## Database Flow Diagram

![DB Flow Diagram](/readme-images/read-me/DB-flow-diagram.png)

# Database Schema

## Changes since the Initial Design

### Many-to-Many Relationship Between `Workout` and `Exercise`
The many-to-many relationship between `Workout` and `Exercise` is implemented using a separate junction table called `WorkoutExercise`. This table stores the associations between specific workouts and their related exercises, along with additional fields such as `sets`, `reps`, `week`, and `day` to track detailed workout plans.

This design avoids storing exercises as a direct foreign key in the `Workout` table, ensuring flexibility and scalability.

### Renaming of User-Related Tables and Fields
- The `User` table retains core user details, but user-specific workout data is stored in a related `Profile` table to separate general user information from domain-specific data.
- The `User` table includes fields like `user_name`, `email`, and `password` and is handeled by `allAuth`.

### Enhanced Workout Fields
Several enhancements were made to the `Workout` table to provide richer metadata:
1. **`owner`:** A foreign key to the `User` table, linking each workout to the user who created it.
2. **`sport`, `level`, and `fitness`:** Foreign keys to respective tables, categorizing the workout by type, difficulty, and fitness focus.
3. **`week_descriptions`:** A field to store narrative descriptions for workout plans.

---

## Updated Flow Diagram

The database schema is better visualized through the flow diagram, showcasing the following tables and their relationships.

---

## Key Tables and Relationships

### **User**
The `User` table stores basic user information required for authentication and identification.

#### **Fields:**
- `user_id` (Primary Key)
- `user_name`
- `email`
- `password`

#### **Relationships:**
- One-to-one with the `Profile` table.
- Related to orders via the `Order` table.

---

### **Profile**
The `Profile` table manages user-specific data, including saved workouts and associated plans.

#### **Fields:**
- `profile_id` (Primary Key)
- `user_id` (Foreign Key)
- `saved_workouts`
- `plan_id` (Foreign Key)

#### **Relationships:**
- Linked to the `User` table (one-to-one).
- Connected to workout plans.

---

### **Workout**
The `Workout` table contains detailed workout plans and metadata.

#### **Fields:**
- `workout_id` (Primary Key)
- `owner` (Foreign Key to `User`)
- `sport` (Foreign Key)
- `level` (Foreign Key)
- `fitness` (Foreign Key)
- `name`
- `description`
- `rating`
- `price`
- `week_descriptions`

#### **Relationships:**
- Many-to-many with the `Exercise` table through the `WorkoutExercise` table.

---

### **WorkoutExercise**
The `WorkoutExercise` junction table handles the many-to-many relationship between `Workout` and `Exercise`.

#### **Fields:**
- `workout_id` (Composite Primary Key and Foreign Key)
- `exercise_id` (Composite Primary Key and Foreign Key)
- `sets`
- `reps`
- `week`
- `day`

---

### **Exercise**
The `Exercise` table defines individual exercises, their execution details, and targeted muscles.

#### **Fields:**
- `exercise_id` (Primary Key)
- `name`
- `main_muscles`
- `secondary_muscles`
- `description`
- `starting_position`
- `execution`
- `tips`
- `equipment`
- `image`
- `image_url`

#### **Relationships:**
- Linked to body parts through the `main_muscles` and `secondary_muscles` fields.
- Many-to-many relationship with the `Workout` table.

---

### **BodyPart**
The `BodyPart` table provides details on muscle groups and their interconnections.

#### **Fields:**
- `bodypart_id` (Primary Key)
- `name`
- `similar_bodyparts` (Self-referential Many-to-Many)

#### **Relationships:**
- Used by the `Exercise` table to associate exercises with muscles.

---

This structure supports flexibility for managing fitness plans, exercises, and user-specific data, with efficient relationships between components. Let me know if you'd like further elaboration or edits!

# Features

# Testing

## Validator Testing

## Manual Testing

## User Testing

## Bugs

# Known Bugs

# Accesibility

## Lighthouse Score

## Broweser Testing

## Device Testing

### Technologies Used

#### Languages  
- HTML5  
- CSS3  
- Python  
- JavaScript  

#### Frameworks, Libraries, and Programs Used  

**Programs**  
- **Chrome DevTools** – Used for overall development and testing, including responsiveness and performance optimization.  
- **GitHub** – Used for version control and storing the project's codebase.  
- **W3C Validators** – Used to validate HTML and CSS for proper syntax and standards compliance.  
- **Responsinator** – Used for testing responsiveness on various devices.  
- **Heroku** – Used for hosting the live website.  

**Frameworks**  
- **Django** – Used as the primary backend framework for routing, authentication, and data management.  
- **Django Allauth** – Integrated for user authentication and account management.  
- **Crispy Forms** – Used for better styling and layout of forms.  

**Libraries**  
- **Boto3** – Used for interacting with Amazon S3 for media and static file storage.  
- **Stripe** – Implemented for handling payment processing.  

**Database**  
- **PostgreSQL** – Used as the relational database for storing and managing application data in production.  
- **SQLite** – Used as the default database during development.  

# Deployment

This website was deployed using Heroku. Follow the steps below to deploy your Django project:

## Prerequisites

Ensure your project includes the following files:

- `Procfile`
- `requirements.txt`
- `runtime.txt`

## Steps to Deploy

1. **Navigate to Heroku**

   - Log in to your Heroku account.

2. **Create a New App**

   - Click on **New** -> **Create new app**.
   - Add a unique app name and select your region.

3. **Set Config Vars**

   - Navigate to the **Settings** tab.
   - Under **Config Vars**, click **Reveal Config Vars**.
   - Add the following variables used in your `env.py` file:
     - `AWS_ACCESS_KEY_ID`
     - `AWS_SECRET_ACCESS_KEY`
     - `DATABASE_URL`
     - `DEVELOPMENT`
     - `EMAIL_HOST_PASS`
     - `EMAIL_HOST_USER`
     - `SECRET_KEY`
     - `STRIPE_PUBLIC_KEY`
     - `STRIPE_SECRET_KEY`
     - `STRIPE_WH_SECRET`
     - `USE_AWS`

4. **Deploy the Project**

   - Navigate to the **Deploy** tab.
   - Connect your app to your GitHub repository by selecting **GitHub** as the deployment method and linking your repository.
   - Enable automatic or manual deploys.

5. **Run the Initial Setup Commands**

   - Navigate to the **More** dropdown and select **Run Console**.
   - Enter the following commands to migrate the database and collect static files:
     ```bash
     python3 manage.py migrate
     python3 manage.py collectstatic
     ```

### Additional Notes

To create a superuser for your Django admin panel:

1. Navigate to the **Run Console** in Heroku.
2. Run the following commands:
   ```bash
   python3 manage.py createsuperuser
   ```
3. Follow the prompts to create your admin account.

---

## Setting up AWS to Store Static Files

To configure AWS S3 for storing static and media files, follow these steps:

1. **Sign Up for AWS**

   - Go to [AWS](https://aws.amazon.com/) and create an account.

2. **Create an S3 Bucket**

   - In the AWS Management Console, navigate to the S3 service and create a new bucket.
   - Configure the bucket:
     - Disable **Block Public Access**.
     - Set **Bucket Policy** to allow public access to static files.
     - Add a **CORS Configuration** to allow your app to access the files.

3. **Set Up IAM Credentials**

   - Navigate to the IAM service and create a new user with **Programmatic Access**.
   - Assign the user to a group with `AmazonS3FullAccess` permissions.
   - Save the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.

4. **Add AWS to Your Django Project**

   - Install `boto3` and `django-storages`:
     ```bash
     pip install boto3 django-storages
     ```
   - Update your `settings.py` to configure `AWS_STORAGE_BUCKET_NAME` and other required settings.
   - Create a `custom_storages.py` file in your project directory with the following content:
     ```python
     from django.conf import settings
     from storages.backends.s3boto3 import S3Boto3Storage

     class StaticStorage(S3Boto3Storage):
         location = settings.STATICFILES_LOCATION

     class MediaStorage(S3Boto3Storage):
         location = settings.MEDIAFILES_LOCATION
     ```

5. **Add Config Vars in Heroku**

   - Add `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `USE_AWS` to Heroku Config Vars.

---

## Signing Up to Stripe and Setting Up Keys and Endpoint

1. **Create a Stripe Account**

   - Sign up at [Stripe](https://stripe.com/).

2. **Get Your API Keys**

   - In the Stripe dashboard, navigate to **Developers** -> **API Keys**.
   - Copy the **Publishable Key** and **Secret Key**.

3. **Set Up Webhook Endpoint**

   - In the Stripe dashboard, navigate to **Developers** -> **Webhooks**.
   - Click **Add Endpoint**.
   - Enter the endpoint URL for your deployed app (e.g., `https://your-app-name.herokuapp.com/stripe/webhook/`).
   - Select the relevant events (e.g., `checkout.session.completed`).
   - Save the webhook.
   - Copy the **Webhook Signing Secret**.

4. **Add Config Vars in Heroku**

   - Add the following variables to Heroku Config Vars:
     - `STRIPE_PUBLIC_KEY`
     - `STRIPE_SECRET_KEY`
     - `STRIPE_WH_SECRET`

5. **Update Your Django Project**

   - Add the Stripe keys to your `settings.py`.
   - Ensure your webhook view is set up to handle events securely.


# Features left to develop 

## Better tracking for workouts. 

With more time i would add better tracking of a users tracked workout. Adding buttons for the user to tick off completed exercises and completed days. 

then when  a user logs back in and clicks track workout they will go straight to the day they are next on. 

## Social presence to the website 

As one of the main aims is the social element of the site and sharing workouts. id like to add a social media element to the site where people can make posts about workouts and or specific exercises they have tried. 

users could add eachother and see what workouts there friends are urrently doing and the posts they have sent eachother 

# Credits 

## Content 

As a passionate fitness enthusiast, I’ve always enjoyed helping my friends get started on their fitness journey. I frequently found myself creating workout plans for them, often writing them out by hand or using basic note apps. However, I realized there was a need for a more efficient and engaging way to share workouts. That’s why I created this app—to provide an easy-to-use platform where you can design personalized workout plans and share them effortlessly.

This app is designed to be a valuable resource for beginners, offering detailed explanations and diagrams for each exercise. It helps eliminate confusion and provides the guidance they need to build confidence in their workouts.

For intermediate and advanced users, the app includes a social element that fosters inspiration and collaboration. Users can discover new ideas from workouts their friends have shared, try out routines created by others, or simply follow along with their friends' plans. It’s a tool that not only supports individual fitness goals but also builds a sense of community and shared progress.

## Resources used:

## Thanks to my Tutors at Code institute.