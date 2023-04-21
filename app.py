# author -- Harsh Kumar
# date 09/apr/2023ls
# importing libraries
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup as bs
import pymongo 
from urllib.request import urlopen as uReq
import logging
logging.basicConfig(filename="scrapper.log", level=logging.INFO)

app = Flask(__name__)

# route to homepage


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
@cross_origin()
# function for homepage
def homepage():
    return render_template('home.html')

# route to result page


@app.route('/result', methods=['GET', 'POST'])
@cross_origin()
# function for result page
def result():
    if request.method == 'POST':
        try:
            # take the entered search string from the form
            SearchString = request.form['search'].replace(' ', '')
            flipkart_url = "https://www.flipkart.com/search?q=" + SearchString
            Client = uReq(flipkart_url)
            flipkart_page = Client.read()
            Client.close()
            flipkart_html = bs(flipkart_page, 'html.parser')
            big_boxes = flipkart_html.find_all('div', {"class": "_1AtVbE col-12-12"})
            # getting link for each specific big box
            del big_boxes[0:3]
            box = big_boxes[0]
            productLink = "https://www.flipkart.com" + box.div.div.div.a['href']       
            prodRes = requests.get(productLink)
            prodRes.encoding='utf-8'
            prod_html = bs(prodRes.text, "html.parser")
            commentboxes = prod_html.find_all('div', {'class': "_16PBlm"})
            
            filename = SearchString+".csv"
            fw = open(filename, "w")
            headers = "Product, Customer Name, Rating, Heading, Comment \n"
            fw.write(headers)
            reviews = []
            for commentbox in commentboxes:
                try:
                    #name.encode(encoding='utf-8')
                    name = commentbox.div.div.find_all('p', {'class': '_2sc7ZR _2V5EHH'})[0].text

                except:
                    logging.info("name")

                try:
                    #rating.encode(encoding='utf-8')
                    rating = commentbox.div.div.div.div.text


                except:
                    rating = 'No Rating'
                    logging.info("rating")

                try:
                    #commentHead.encode(encoding='utf-8')
                    commentHead = commentbox.div.div.div.p.text

                except:
                    commentHead = 'No Comment Heading'
                    logging.info(commentHead)

                try:
                    comtag = commentbox.div.div.find_all('div', {'class': ''})
                    #custComment.encode(encoding='utf-8')
                    custComment = comtag[0].div.text
                except Exception as e:
                    logging.info(e)
                    
                    
                prod_rev_details = {"Product": SearchString, "Name": name,
                                    "Rating": rating, "CommentHeader": commentHead, "Comment": custComment}
                reviews.append(prod_rev_details)

            msg = "Successfully Scrapped data"
            logging.info("Final Result{}".format(reviews))
            #connecting to mongo db
            #change <cluster_link> with your mongodb clusterlink
           
            client = pymongo.MongoClient("mongodb+srv://<cluster_link>")
            db = client['scrapper_eng']
            coll_eng = db['scrapper']
            coll_eng.insert_many(reviews)
            return render_template('result.html', reviews=reviews[0:(len(reviews)-1)], msg=msg)
        except Exception as e:
            logging.info(e)
            return 'Kush to Gadbad hai Daya !!!!'

    else:
        msg = 'No string searched yet'
        return render_template('result.html', msg=msg)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug='True')
