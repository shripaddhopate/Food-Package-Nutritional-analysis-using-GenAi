# Food-Package-Nutritional-analysis-using-GenAi

## Project Overview

This project leverages Generative AI to analyze food package nutritional values and ingredients. Users can upload an image of a food package, and feeding it to an LLM model (Gemini API). The model then evaluates whether the food is healthy and provides insights on its impact by extracting relevant nutritional information.

## Features

  - Image Upload: Users upload an image of a food package containing nutritional values and ingredient lists.
  - LLM Analysis: The Gemini Multimodel API is used to assess health impacts.
  - User Interface: The project uses Tinkeract for a seamless and interactive UI.
  - Health Score & Insights: The model provides an assessment score and recommendations based on the extracted nutritional data.

## Technologies Used

- Python: Core development language
- Tinkeract: User interface framework
- Gemini API: LLM for food analysis and recommendations


## Installation

- Clone the repository:
git clone https://github.com/shripaddhopate/Food-Package-Nutritional-analysis-using-GenAi.git
- cd food-nutrition-analysis
- git checkout develop
- Set up API keys:
- Configure the Gemini API key in an .env file or as an environment variable.
- Run the application:
- python main.py
- Launch the application.
- The system provides a health assessment and recommendations.


## Future Improvements

- Implement support for multiple languages in OCR.
- Enhance UI with a web-based front-end.
- Integrate a database for historical analysis of food choices.
- Add a chatbot for personalized dietary recommendations.

## Contributing
If you'd like to contribute, feel free to fork the repository and submit a pull request.


