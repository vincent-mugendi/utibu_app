# Proposed Solution

- The following are solutions I'm proposing to address the requirements outlined for the Utibu Health Mobile App. I'm considering both my expertise and the most effective ways to achieve the desired outcomes  

## Frontend
- **Use React Native for cross-platform compatibility and a native-like user experience.**
  - **Reasoning:** 
    - React Native allows for the development of cross-platform mobile apps that can run on both iOS and Android, 
    - This reduces development time and effort. 
    - It also provides a native-like user experience and thus enhances the app's usability and performance.

## Backend
- **Implement a Python Flask server to handle business logic and interact with the Microsoft SQL Server database.**
  - **Reasoning:** 
    - Flask is a lightweight and easy-to-use web framework
    - It is well-suited for building the backend of a mobile app. 
    - It allows for quick implementation of the required APIs and integrates seamlessly with the Microsoft SQL Server database.

## Database
- **Utilize Microsoft SQL Server for data storage, as it aligns with the legacy system and provides a familiar environment.**
  - **Reasoning:** 
    - Microsoft SQL Server is already used in the legacy system, ensuring compatibility and ease of integration. 
    - It also provides a familiar environment for developers, making it easier to work with and maintain.

## Integration
- **Use RESTful APIs for communication between the mobile app and the backend, to ensure secure and efficient data exchange.**
  - **Reasoning:** 
    - RESTful APIs provide a lightweight and scalable way to communicate between the frontend and backend. 
    - Their security and efficiency enhance the overall performance of the app.

## Security
- **Implement HTTPS to protect data in transit. Also use OAuth for user authentication to enhance security.**
  - **Reasoning:** 
    - Security is paramount when dealing with sensitive medical and financial information.
    - HTTPS helps protect data in transit, while OAuth provides a secure way to authenticate users.

## User Experience
- **Design the app's UI/UX using Figma for a modern and intuitive interface that meets the needs of Utibu health's customers.**
  - **Reasoning:** 
    - Figma will help me figure the look and feel of the app before i go ahead into coding 

## Offline Support
- **Implement offline capabilities in the mobile app to allow users to place orders and check statements even when not connected to the internet. Use local storage to store data temporarily and sync with the server when online.**
  - **Reasoning:** 
    - I believe Offline support is crucial for a mobile app in a healthcare setting, where internet connectivity may be unreliable. 
    - Implementing offline capabilities allows users to continue using the app even when offline, enhancing accessibility and user satisfaction.

# Possible Bottlenecks and Decisions Made

## Legacy System Integration
- **Integrating with the legacy system may be challenging due to its outdated technology stack. However, using a RESTful API approach allows for decoupling the mobile app from the legacy system, reducing dependencies and potential bottlenecks.**
  - This approach will also make it easier to maintain and update the app in the future.

## Database Performance
- **The Microsoft SQL Server may experience performance issues when handling a large number of concurrent requests. To mitigate this, I suggest optimizing database queries and consider implementing caching mechanisms.**


## Security Concerns
- **Since the app deals with sensitive medical and financial information, security is paramount. Implementing secure communication protocols and regular security audits can help address these concerns.**
