from flask import Flask, render_template
import pandas as pd
import numpy as np
import plotly
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import json


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/attack')
def analysis():
    df = pd.read_csv('Updated.csv')
    df['Month'].replace('JUN ','JUN',inplace=True)
    df['Month'].replace(0,np.nan,inplace=True)
    df['Month'].dropna(inplace=True)
    month = df['Month'].value_counts()
    fig1 = px.bar(df,x=month.index.values,y=month.values,color=month.index.values,title='Ransomware Attack According to Months',
                    labels={'x':'Month','y':'No. of attacks'})
    graph1=json.dumps(fig1,cls=plotly.utils.PlotlyJSONEncoder)

    rp=df['Ransom Paid'].value_counts()
    fig2 = px.pie(df,names=rp.index.values,values=rp,title='Ransom Paid')
    graph2=json.dumps(fig2,cls=plotly.utils.PlotlyJSONEncoder)

    r=df['YEAR'].value_counts()
    fig3 = px.pie(df,names=r.index.values,values=r,title='YEAR')
    graph3=json.dumps(fig3,cls=plotly.utils.PlotlyJSONEncoder)

    fig4=px.scatter(df,y='Top ransomware attacks',x='Revenue',color='Top ransomware attacks',title='Ransomware Attack According to Revenue')
    graph4=json.dumps(fig4,cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('attack.html',graph1=graph1,graph2=graph2,graph3=graph3,graph4=graph4)

@app.route('/attack-2')
def analysis_1():
    df = pd.read_csv('Updated.csv')
    df['Sector'].replace('finace','finance',inplace=True)
    df['Sector'].replace('telecomms','telecoms',inplace=True)
    df['Sector'].replace('tech ','tech',inplace=True)
    rev = df['Revenue'].value_counts()
    fig5 = px.bar(df,x=rev.index.values,y=rev.values,color=rev.index.values,title='Revenue',
                    labels={'x':'Revenue','y':'No. of attacks'})
    graph5=json.dumps(fig5,cls=plotly.utils.PlotlyJSONEncoder)

    fig6 = px.bar(df,y='Ransom Paid',x='Sector',color='Sector',title='Ransom Paid According to Sector')
    graph6=json.dumps(fig6,cls=plotly.utils.PlotlyJSONEncoder)

    fig7 = px.scatter(df,y='Organisation Size',x='Top ransomware attacks',color='Organisation Size',
                        title='Ransomware Attack According to Organisation Size', height=600)
    graph7=json.dumps(fig7,cls=plotly.utils.PlotlyJSONEncoder)

    fig8 = px.bar(df,y='Organisation Size',x='Top ransomware attacks',color='Organisation Size',
                    title='Ransomware Attack According to Organisation Size', height=600)
    graph8=json.dumps(fig8,cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('attack-2.html',graph5=graph5,graph6=graph6,graph7=graph7,graph8=graph8)


@app.route('/attack-3')
def analysis_3():
    df = pd.read_csv('Updated.csv')
    fig9 = px.histogram(df,x='Organisation Size', marginal='box',title='Organisation Size')
    graph9=json.dumps(fig9,cls=plotly.utils.PlotlyJSONEncoder)

    fig10 = px.scatter(df,y='Top ransomware attacks',x='Ransom Cost',color='Top ransomware attacks',title='Ransomware Attack Cost')
    graph10=json.dumps(fig10,cls=plotly.utils.PlotlyJSONEncoder)
    
    fig11 = px.scatter(df,y='YEAR',x='Top ransomware attacks',color='YEAR',title='Ransomware Attack Yearwise Representation', height=600)
    graph11=json.dumps(fig11,cls=plotly.utils.PlotlyJSONEncoder)

    sec = df['Sector'].value_counts()
    fig12 = px.bar(df,y= sec.index.values,x=sec.values,color=sec,title='Sectors Attacked',
                    labels={'x':'No. of attacks','y':'Sector'})
    graph12=json.dumps(fig12,cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('attack-3.html',graph9=graph9,graph10=graph10,graph11=graph11,graph12=graph12)


@app.route('/attack-4')
def analysis_4():
    df = pd.read_csv('Updated.csv')
    fig13 = px.bar(df,x='Sector',y='Ransom Cost',color='Sector',title='Ransome Cost Sector Wise')
    graph13=json.dumps(fig13,cls=plotly.utils.PlotlyJSONEncoder)

    fig14 =px.scatter(df,y='Top ransomware attacks',x='Location',color='Top ransomware attacks',title='Ransome Attacks Location Wise')
    graph14=json.dumps(fig14,cls=plotly.utils.PlotlyJSONEncoder)

    fig15 = px.line(df,y='Location',x='Top ransomware attacks',color='Location',title="Ransome Attacks Location Wise")
    graph15=json.dumps(fig15,cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('attack-4.html',graph13=graph13,graph14=graph14,graph15=graph15)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 