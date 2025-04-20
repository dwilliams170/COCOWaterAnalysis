import matplotlib.pyplot as plt

def make_plot(sentiments: list) -> list:

    """
    Examines the list of reviews and plots the amount of each sentiment (`positive`, `neutral`, `negative`, and `irrelevant)
    
    Args: 
        supplies a list of strings(reviews) to determine the number of positive, negative, neutral or irrelevant reviews
    
    Returns: 
        a bar graph with the number of sentiments (positive, negative, neutral or irrelevant) reviews
    
    """
    # Counts the number of each sentiment reviews
    reviews_count = {}
    
    for sentiment in sentiments:
        current_count = reviews_count.setdefault(sentiment,0)
        reviews_count[sentiment] = current_count + 1 
    
    #Note - return reviews_count - will cause an error/not show data

    #Colors to coordinate with the reviews
   
    colors = ['red','green', 'grey', 'purple'] 
    
    #Creates the bar graph
    
    fig,ax = plt.subplots()
    
    #sets title, x-axis and y-axis labels
    ax.bar(reviews_count.keys(),reviews_count.values(),color = colors)
   
        
    ax.set_title("Sentiment Analysis")
    ax.set_xlabel("Reviews")
    ax.set_ylabel("Sentiment Count")
    
    #labels the number of reviews in each sentiment
    
    for index,value in enumerate(reviews_count.values()):
        ax.text(index, value + 0.1, str(value), ha = 'center')
    
    #Saves bar graph as png
    fig.savefig("images/reviews_analysis.png")
   
    
