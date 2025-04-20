
# OpenAI Review Auto-Evaluation - COCO Water Review Process 🚰

Create a minimal pipeline tool that will read a JSON file of reviews and automatically generate an output file that contains the following sentiment labels: 

✅ Positive

⚠️ Neutral

⛔ Negative

🚫 Irrelevant

This tool utilizes the GPT-4o-mini model from the OpenAI's API. The API adheres to token limitations and specific requests. 

## Installation

Dependencies: Environement(ds), OpenAI API Key, Miniconda

1) Activate your Conda Environment via the terminal command:

 ```python test_package.py ``` 

2) Confirm that you can see the (ds) prompt at the beginning of your environment. 

3) After you have confirmed that you are in the environment, set your given API key to your Conda environment variable using the following command:
   
``` conda env config vars set OPENAI_API_KEY="your_api_key" ``` 

5) Deactivate and reactivate your Conda environment using the commands in your terminal:
   
```conda deactivate conda activate ds ``` 

7) Next, install the OpenAI package by running the pip command in your terminal: 

```pip install openai ``` 

6) Run the test_package.py module to check if your OpenAI package is functioning properly: 

```python test_package.py ``` 

7) You should see your terminal output: Success!
```Success!``

## Files to Edit

```label.py ```

```visualize.py```

```main.py```

```writeup.md``` 

## Example:

The example input contains the following arrays of reviews:

[
 "this ring smells weird, don't recomend",
 "I love this ring, I use it all the time when working out.",
 "I will never buy another brand again, I love this ring",
 "It's an ok ring. Some features could be better but for the price its fine.",
 "its a ring",
 "Bought this ring and it came broken. rip-off."
]

The program would output the following sentiment labels: 

["negative", "positive", "positive", "neutral", "irrelevant", "negative"]


## Documentation

[Sentiment Analysis](https://en.wikipedia.org/wiki/Sentiment_analysis)

[OPENAI API](https://platform.openai.com/docs/libraries?desktop-os=windows&language=python)

[API Text generation and prompting](https://platform.openai.com/docs/guides/text?api-mode=responses)

[MiniConda Installation](https://platform.openai.com/docs/guides/text?api-mode=responses)


## Author

- [Darylisha Williams](https://github.com/dwilliams170)


## Lessons Learned

❗ System prompt design is important. Please pay attention to your prompting in your open ai API while using the chat.completions.create() method. 

❗The reviews.json file contains only 50 reviews, but the final visualization displayed more than what was included in the JSON file. 


