@app.route("/scrape")
def scrape():
    global baseURL
    global output_data
    table_name = baseURL.split("?")[0]
    conn = sql.connect('database.db')

    c = conn.cursor()
    c.execute('''SELECT count(name) FROM sqlite_master WHERE name='%s' AND type='table' '''%table_name)

    if(c.fetchone()[0]==0):

        scrape_with_crochet(baseURL=baseURL)
        time.sleep(10)

        conn.execute('''CREATE TABLE '%s' (names TEXT,  reviewerLink TEXT, reviewTitles TEXT, reviewBody TEXT, verifiedPurchase TEXT, postDate TEXT, starRating TEXT, helpful TEXT, nextPage TEXT)''' %table_name)
        
        for x in output_data:
            c.execute('''INSERT INTO '%s' (names, reviewerLink, reviewTitles, reviewBody, verifiedPurchase, postDate, starRating, helpful, nextPage) VALUES (?,?,?,?,?,?,?,?,?)''' %table_name ,(x["names"], x["reviewerLink"], x["reviewTitles"], x["reviewBody"], x["verifiedPurchase"], x["postDate"], x["starRating"], x["helpful"], x["nextPage"]))
        
        conn.commit()
        conn.close()

        print("Table and Records created Successfully!")

        
    else: # The code will come here if it doesn't find the URL data in DB
        conn.row_factory = sql.Row
        cur = conn.cursor()
        cur.execute(''' SELECT * from '%s' '''%table_name)

        rows = cur.fetchall()
        output_data = ([dict(i) for i in rows])

        conn.close()

        print("Data Fetched Successfully!")

    return jsonify(output_data)