## Flask Application Design

### HTML Files

- **index.html**: The main page of the application, serving as the dashboard for FSRs. It should contain the necessary HTML elements to display performance metrics and sales play data.
- **sales_plays.html**: A page dedicated to providing detailed information about sales plays, including graphs, charts, and relevant metrics.
- **book_of_business.html**: A page displaying data and insights related to the FSR's Book of Business, including customer profiles and performance tracking.
- **performance_dashboards.html**: A dynamic page that allows FSRs to view personalized performance dashboards tailored to their roles and responsibilities.

### Routes

- **@app.route('/')**: The route for the main dashboard page (index.html).
- **@app.route('/sales_plays')**: The route for the sales plays page (sales_plays.html).
- **@app.route('/book_of_business')**: The route for the Book of Business page (book_of_business.html).
- **@app.route('/performance_dashboards')**: The route for the performance dashboards page (performance_dashboards.html).
- **@app.route('/api/sales_plays')**: An API endpoint that provides sales play data in JSON format for use in charts and graphs.
- **@app.route('/api/book_of_business')**: An API endpoint that provides Book of Business data in JSON format for use in customer profiles and performance tracking.
- **@app.route('/api/performance_data')**: An API endpoint that provides personalized performance data based on the FSR's role and responsibilities.