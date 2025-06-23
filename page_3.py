def get_page_html(form_data=None): 

    page_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Australian Climate Change Analysis | Bureau of Meteorology</title>
        <meta name="description" content="Explore Australian climate change data from 1970-2020 through Bureau of Meteorology weather stations">
        <link rel="stylesheet" href="timeperiod_comparison.css">
        <link href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
        <style>
            .textbox {
                width: 100%; /* Adjust width as needed */
                padding: 8px; /* Adjust padding for less chubbiness */
                box-sizing: border-box; /* Ensure padding is included in width */
                border: 1px solid #ccc; /* Add border for better appearance */
                border-radius: 4px; /* Slightly rounded corners */
            }
        </style>
    </head>
    <body>
    <header class="main-header">
        <div class="header-content">
            <div class="logo-section">
                <img src="logo.png" alt="Bureau of Meteorology Logo" class="logo">
                <h1>Bureau of Meteorology</h1>
            </div>
            <nav class="main-nav">
                <ul>
                    <li><a href="home.html">Home</a></li>
                    <li><a href="observations.html">Weather Stations</a></li>
                    <li><a href="#" class="active">Observations</a></li>
                    <li><a href="#">Climate Data</a></li>
                    <li><a href="#">About</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <section class="background-banner">
        <img src="resources/Dark.jpg" alt="Autumn in Australia" class="autumn">
            <div class="vignette-box">
                <form action="/observations.html" method="POST">
                    <div class="subtitle-container">
                        <p class="subtitle-text">First time period</p>
                    </div>
                    <div class="input-container">
                        <div class="to">
                            <input type="text" name="start_year_1" placeholder="Start year" class="textbox"> 
                            <p class="subtitle-text">to</p>
                        </div>
                        <input type="text" name="end_year_1" placeholder="End year" class="textbox">
                    </div>
                    <div class="empty-space"></div>
                    <div class="subtitle-container">
                        <p class="subtitle-text">Second time period</p>
                    </div>
                    <div class="input-container">
                        <div class="to">
                            <input type="text" name="start_year_2" placeholder="Start year" class="textbox"> 
                            <p class="subtitle-text">to</p>
                        </div>
                        <input type="text" name="end_year_2" placeholder="End year" class="textbox">
                    </div>

                    <div class="empty-space"></div>
                    <div class="subtitle-container">
                            <p class="subtitle-text">Reference weather station</p>
                    </div>
                    <div class="input-container">
                        
                        <input type="text" name="station_name" placeholder="Weather station name" class="textbox">
                    </div>

                    <div class="empty-space"></div>

                    <div class="subtitle-container">
                        <p class="subtitle-text">Metric comparison</p>
                    </div>
                    <div class="radio-group">
                        <div class='radio-item'>
                            <div class='whatever'>
                                <p class="radiobutton-text">Temperature</p>
                                <input type="radio" name="metric" value="Temperature" class="radio-button">
                            </div>
                        </div>
                        <div class='radio-item'>
                            <div class='whatever'>
                                <p class="radiobutton-text">Rainfall</p>
                                <input type="radio" name="metric" value="Rainfall" class="radio-button">
                            </div>
                        </div>
                        <div class='radio-item'>
                            <div class='whatever'>
                                <p class="radiobutton-text">Humidity</p>
                                <input type="radio" name="metric" value="Humidity" class="radio-button">
                            </div>
                        </div>
                        <div class='radio-item'>
                            <div class='whatever'>
                                <p class="radiobutton-text">Windspeed</p>
                                <input type="radio" name="metric" value="Windspeed" class="radio-button">
                            </div>
                        </div>
                    </div>

                    <div class="empty-space"></div>
                    <div class="subtitle-container">
                        <p class="subtitle-text">No. Stations Compared</p>
                    </div>
                    <div class="input-container">   
                        <input type="text" name="num_stations" placeholder="No. Stations" class="textbox">
                    </div>

                    <div class="empty-space"></div>

                    <div class="submit-container">
                        <button class="submit">Submit</button>
                    </div>
                </form>
            </div>
    </section>

    <section class="white-dashboard">
        <ul class="dashboard-list">
            <li>Weather Station</li>
            <li>Average Temp (2005-2009)</li>
            <li>Average Temp (2010-2015)</li>
            <li>Change(%)</li>
            <li>Difference from Melbourne Airport(%)</li>
        </ul>
    </section>
    <hr>

    <section class="results-description1">
        <ul class="entries-list">
            <li>Melbourne Airport</li>
            <li>22.5</li>
            <li>22.7</li>
            <li>+0.88</li>
            <li>+0.00</li>
        </ul>
    </section>
    <hr>

    <section class="results-description2">
        <ul class="entries-list">
            <li>Ballarat</li>
            <li>17.2</li>
            <li>17.6</li>
            <li>+0.23</li>
            <li>-0.65</li>
        </ul>
    </section>
    <hr>

    <section class="results-description1">
        <ul class="entries-list">
            <li>Bendigo</li>
            <li>16.9</li>
            <li>17.0</li>
            <li>+0.59</li>
            <li>-0.29</li>
        </ul>
    </section>
    <hr>

    <footer>
        <div class="footer-content">
            <p>&copy; 2025 Bureau of Meteorology - Climate Change Analysis</p>
            <p>Quality-controlled climate data from 1970 to 2020</p>
        </div>
    </footer>
</body>
</html>
"""
    return page_html