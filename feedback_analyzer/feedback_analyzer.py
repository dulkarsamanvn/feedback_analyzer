import pandas as pd
from transformers import pipeline


def analyze_feedback(input_file,output_file):
    df=pd.read_csv(input_file)
    sentiment_pipeline=pipeline('sentiment-analysis')

    scores=[]
    sentiments=[]

    for text in df['feedback']:
        result=sentiment_pipeline(text)[0]
        sentiments.append(result['label'])
        scores.append(round(result['score'],2))

    df['sentiments']=sentiments
    df['scores']=scores

    df.to_csv(output_file,index=False)
    print(f"Analysis complete! Results saved to {output_file}")

if __name__=='__main__':
    analyze_feedback('feedback.csv','results.csv')



