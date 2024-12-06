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

#### General Users

- **First-time Users**:
  - "As a first-time user, I want the platform to guide me through creating and sharing my first workout plan."
  - "As a first-time user, I want to explore the exercise library to find ideas and instructions for my fitness routine."

- **Frequent Users**:
  - "As a frequent user, I want to save and track my progress on workouts I’ve tried."
  - "As a frequent user, I want to leave reviews and ratings for workouts I’ve completed."

#### Donors

- "As a donor, I want my custom username tag to stand out in the community, showing my support for the platform."


# Design 

## Imagery

### Color Scheme 

### Layout 

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
