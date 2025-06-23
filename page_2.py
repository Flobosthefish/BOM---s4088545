import sqlite3
from datetime import datetime

def get_page_html(form_data=None):
    base_page_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Australian Climate Change Analysis | Bureau of Meteorology</title>
        <meta name="description" content="Explore Australian climate change data from 1970-2020 through Bureau of Meteorology weather stations">
        <link rel="stylesheet" href="observations.css">
        <link href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
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
                        <li><a href="#" class="active">Weather Stations</a></li>
                        <li><a href="timeperiod_comparison.html">Observations</a></li>
                        <li><a href="#">Climate Data</a></li>
                        <li><a href="#">About</a></li>
                    </ul>
                </nav>
            </div>
        </header>
        <header class="background-banner">
            <img src="resources/Autumn photo.jpg" alt="Autumn in Australia" class="autumn">
            <div class="vignette-box">
                <div class="empty-space"></div>
                <div class="subtitle-container">
                    <p class="subtitle-text">Enter start latitude</p>
                    <p class="subtitle-text">Enter end latitude</p>
                </div>
                <form action="/observations.html" method="POST">
                    <div class="input-container">
                        <div class="to">
                            <input type="number" step="1" min="-90" max="90" 
                                   placeholder="-35.000000" class="textbox" name="lat-min" 
                                   value="{lat_min_value}" required>
                            <p class="subtitle-text">to</p>
                        </div>
                        <input type="number" step="1" min="-90" max="90" 
                               placeholder="-30.000000" class="textbox" name="lat-max" 
                               value="{lat_max_value}" required>
                    
                    </div>
                    <div class="subtitle-container">
                        <p class="subtitle-text">Select Date</p>
                    </div>
                    <div class="input-container">
                        <input type="date" class="textbox" name="start_date" value="{start_date_value}" required min="1970-01-01" max="2020-12-31">
                    </div>
                    <div class="empty-space"></div>
                    <div class="subtitle-container">
                        <p class="subtitle-text">Select Climate Metrics to Display</p>
                        <p class="subtitle-text">Select States</p>
                    </div>
                    <div class="radio-container">
                        <div class="radio">
                            <div class="checkbox-container">
                                <p class="checkbox-text">Precipitation</p>
                                <input type="checkbox" name="metric" value="precipitation" 
                                       class="checkbox" {precipitation_checked}>
                            </div>
                            <div class="checkbox-container">
                                <p class="checkbox-text">Evaporation</p>
                                <input type="checkbox" name="metric" value="evaporation" 
                                       class="checkbox" {evaporation_checked}>
                            </div>
                            <div class="checkbox-container">
                                <p class="checkbox-text">Temperature</p>
                                <input type="checkbox" name="metric" value="temperature" 
                                       class="checkbox" {temp_checked}>
                            </div>
                            <div class="checkbox-container">
                                <p class="checkbox-text">Humidity</p>
                                <input type="checkbox" name="metric" value="humidity" 
                                       class="checkbox" {humidity_checked}>
                            </div>
                            <div class="checkbox-container">
                                <p class="checkbox-text">Sunshine</p>
                                <input type="checkbox" name="metric" value="sunshine" 
                                       class="checkbox" {sunshine_checked}>
                            </div>
                            <div class="checkbox-container">
                                <p class="checkbox-text">Okta</p>
                                <input type="checkbox" name="metric" value="okta" 
                                       class="checkbox" {okta_checked}>
                            </div>
                        </div>
                        <div class="radio">
                            <div class="checkbox-container">
                                <p class="checkbox-text">NSW</p>
                                <input type="checkbox" name="state" value="nsw" 
                                       class="checkbox" {nsw_checked}>
                            </div>
                            <div class="checkbox-container">
                                <p class="checkbox-text">VIC</p>
                                <input type="checkbox" name="state" value="vic" 
                                       class="checkbox" {vic_checked}>
                            </div>
                            <div class="checkbox-container">
                                <p class="checkbox-text">SA</p>
                                <input type="checkbox" name="state" value="sa" 
                                       class="checkbox" {sa_checked}>
                            </div>
                            <div class="checkbox-container">
                                <p class="checkbox-text">QLD</p>
                                <input type="checkbox" name="state" value="qld" 
                                       class="checkbox" {qld_checked}>
                            </div>
                            <div class="checkbox-container">
                                <p class="checkbox-text">NT</p>
                                <input type="checkbox" name="state" value="nt" 
                                       class="checkbox" {nt_checked}>
                            </div>
                            <div class="checkbox-container">
                                <p class="checkbox-text">TAS</p>
                                <input type="checkbox" name="state" value="tas" 
                                       class="checkbox" {tas_checked}>
                            </div>
                            <div class="checkbox-container">
                                <p class="checkbox-text">WA</p>
                                <input type="checkbox" name="state" value="wa" 
                                       class="checkbox" {wa_checked}>
                            </div>
                            <div class="checkbox-container">
                                <p class="checkbox-text">AET</p>
                                <input type="checkbox" name="state" value="aet" 
                                       class="checkbox" {aet_checked}>
                            </div>
                            <div class="checkbox-container">
                                <p class="checkbox-text">AAT</p>
                                <input type="checkbox" name="state" value="aat" 
                                       class="checkbox" {aat_checked}>
                            </div>
                        </div>
                    </div>
                    <div class="empty-space"></div>
                    <div class="submit-container">
                        <button type="submit" class="submit">Submit</button>
                    </div>
                    <div class="empty-space"></div>
                </form>
                {error_message}
                {success_message}
            </div>
        </header>
        <div id="results_section">
            {results_section}
        </div>

        <script>
        window.onload = function() {{
            var results = document.getElementById('results_section');
            if (results && results.innerText.trim() !== "") {{
                results.scrollIntoView({{ behavior: 'smooth' }});
            }}
        }};
        </script>

        <footer>
            <div class="footer-content">
                <p>&copy; 2025 Bureau of Meteorology - Climate Change Analysis</p>
                <p>Quality-controlled climate data from 1970 to 2020</p>
            </div>
        </footer>
    </body>
    </html>
    """

    # Initialize default values
    lat_min_value = ""
    lat_max_value = ""
    start_date_value = ""
    precipitation_checked_value = ""
    evaporation_checked_value = ""
    temp_checked_value = ""
    humidity_checked_value = ""
    sunshine_checked_value = ""
    okta_checked_value = ""
    qld_checked_value = ""
    aet_checked_value = ""
    aat_checked_value = ""
    nsw_checked_value = "" 
    sa_checked_value = ""
    nt_checked_value = ""
    wa_checked_value = ""
    tas_checked_value = ""
    vic_checked_value = ""
    error_message = ""
    success_message = ""
    results_section = ""

    # If no form data provided, return empty form
    if not form_data:
        return base_page_html.format(
            lat_min_value=lat_min_value,
            lat_max_value=lat_max_value,
            start_date_value=start_date_value,
            precipitation_checked=precipitation_checked_value,
            evaporation_checked=evaporation_checked_value,
            temp_checked=temp_checked_value,
            humidity_checked=humidity_checked_value,
            sunshine_checked=sunshine_checked_value,
            okta_checked=okta_checked_value,
            qld_checked=qld_checked_value,
            aet_checked=aet_checked_value,
            aat_checked=aat_checked_value,
            nsw_checked=nsw_checked_value,
            sa_checked=sa_checked_value,
            nt_checked=nt_checked_value,
            wa_checked=wa_checked_value,
            tas_checked=tas_checked_value,
            vic_checked=vic_checked_value,
            success_message=success_message,
            error_message=error_message,
            results_section=results_section

        )

    # Extract form data (Get lat_min, lat_max, and metrics)
    lat_min = form_data.get('lat-min', [''])[0] if 'lat-min' in form_data else form_data.get('lat_min', [''])[0]
    lat_max = form_data.get('lat-max', [''])[0] if 'lat-max' in form_data else form_data.get('lat_max', [''])[0]
    metrics = form_data.get('metric', [])
    states = form_data.get('state', [])
    states = [word.upper() for word in states]
    print(f"States selected: {states}")
    start_date = form_data.get('start_date', [''])[0] if 'start_date' in form_data else form_data.get('start_date', [''])[0]

    print(f"lat_min: {lat_min}, lat_max: {lat_max}, metrics: {metrics}")

    # Preserve form values
    lat_min_value = lat_min
    lat_max_value = lat_max

    # Parse the submitted date (HTML input: YYYY-MM-DD)
    dt = datetime.strptime(start_date, '%Y-%m-%d')

    # Format for SQL query: DD/MM/YYYY
    formatted_date = f"{dt.day}/{dt.month}/{dt.year}"

    # Keep original format for HTML form (YYYY-MM-DD)
    start_date_value = start_date

    # Checkbox states
    if 'NSW' in states:
        nsw_checked_value = "checked"
    if 'VIC' in states:
        vic_checked_value = "checked"
    if 'SA' in states:
        sa_checked_value = "checked"
    if 'QLD' in states:
        qld_checked_value = "checked"
    if 'NT' in states:
        nt_checked_value = "checked"
    if 'TAS' in states:
        tas_checked_value = "checked"
    if 'WA' in states:
        wa_checked_value = "checked"
    if 'AET' in states:
        aet_checked_value = "checked"
    if 'AAT' in states:
        aat_checked_value = "checked"
    if 'precipitation' in metrics:
        precipitation_checked_value = "checked"
    if 'evaporation' in metrics:
        evaporation_checked_value = "checked"
    if 'temperature' in metrics:
        temp_checked_value = "checked"
    if 'humidity' in metrics:
        humidity_checked_value = "checked"
    if 'sunshine' in metrics:
        sunshine_checked_value = "checked"
    if 'okta' in metrics:
        okta_checked_value = "checked"

    # If no inputs provided, return form without validation
    if lat_min == '' and lat_max == '' and not metrics:
        return base_page_html.format(
            lat_min_value=lat_min_value,
            lat_max_value=lat_max_value,
            start_date_value=start_date_value,
            precipitation_checked=precipitation_checked_value,
            evaporation_checked=evaporation_checked_value,
            temp_checked=temp_checked_value,
            humidity_checked=humidity_checked_value,
            sunshine_checked=sunshine_checked_value,
            okta_checked=okta_checked_value,
            qld_checked=qld_checked_value,
            aet_checked=aet_checked_value,
            aat_checked=aat_checked_value,
            nsw_checked=nsw_checked_value,
            sa_checked=sa_checked_value,  
            nt_checked=nt_checked_value,
            wa_checked=wa_checked_value,  
            tas_checked=tas_checked_value,
            vic_checked=vic_checked_value,
            success_message=success_message,
            error_message=error_message,
            results_section=results_section,
        )

    # Validate inputs
    validation_errors = []

    try:
        if lat_min == '':
            validation_errors.append("Start latitude is required")
        else:
            lat_min_val = float(lat_min)
            if not (-90 <= lat_min_val <= 90):
                validation_errors.append("Start latitude must be between -90 and 90")
    except ValueError:
        validation_errors.append("Start latitude must be a valid number")

    try:
        if lat_max == '':
            validation_errors.append("End latitude is required")
        else:
            lat_max_val = float(lat_max)
            if not (-90 <= lat_max_val <= 90):
                validation_errors.append("End latitude must be between -90 and 90")
    except ValueError:
        validation_errors.append("End latitude must be a valid number")

    # Check if both latitudes are valid for range comparison
    if not validation_errors and lat_min != '' and lat_max != '':
        try:
            lat_min_val = float(lat_min)
            lat_max_val = float(lat_max)
            if lat_min_val > lat_max_val:
                validation_errors.append("Start latitude must be less than or equal to end latitude")
        except ValueError:
            pass  

    if not metrics:
        validation_errors.append("Please select at least one climate metric")

    if not states:
        validation_errors.append("Please select at least one state")

    # If there are validation errors, show them and list them.
    if validation_errors:
        error_message = f"""
        <div class="empty-space"></div>
        <div class="error-container" style="background-color: #ffebee; border: 1px solid #f44336; 
             padding: 15px; margin: 3%; border-radius: 4px;">
            <h3 style="color: #d32f2f; margin-top: 0;">Please correct the following errors:</h3>
            <ul style="color: #d32f2f; margin: 0; list-style-type: none;">
                {''.join(f'<li>{error}</li>' for error in validation_errors)}
            </ul>
        </div>
        """
        return base_page_html.format(
            lat_min_value=lat_min_value,
            lat_max_value=lat_max_value,
            start_date_value=start_date_value,  
            precipitation_checked=precipitation_checked_value,
            evaporation_checked=evaporation_checked_value,
            temp_checked=temp_checked_value,
            humidity_checked=humidity_checked_value,
            sunshine_checked=sunshine_checked_value,
            okta_checked=okta_checked_value,
            qld_checked=qld_checked_value,
            aet_checked=aet_checked_value,
            aat_checked=aat_checked_value,
            nsw_checked=nsw_checked_value,
            sa_checked=sa_checked_value,  
            nt_checked=nt_checked_value,
            wa_checked=wa_checked_value,  
            tas_checked=tas_checked_value,
            vic_checked=vic_checked_value,
            error_message=error_message,
            success_message=success_message,
            results_section=results_section
        )

    # Connect to location.db and query data safely
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    print(cursor.execute("SELECT * FROM sqlite_schema").fetchall())
    # Use parameterized query to avoid SQL injection
    placeholders = ', '.join('?' for _ in states)

    query = '''
        SELECT t1.Site, t1.Name, t1.Lat, t1.Long, t2.precipitation, t2.evaporation, t2.MinTempQual, t2.MaxTemp, 
(COALESCE(Humid00Qual, 0) + COALESCE(Humid03Qual, 0) + COALESCE(Humid06Qual, 0) + COALESCE(Humid09Qual, 0) + 
COALESCE(Humid12Qual, 0) + COALESCE(Humid15Qual, 0) + COALESCE(Humid18Qual, 0) + COALESCE(Humid21Qual, 0)) 
/
  NULLIF(
    (CASE WHEN Humid00Qual IS NOT NULL THEN 1 ELSE 0 END +
     CASE WHEN Humid03Qual IS NOT NULL THEN 1 ELSE 0 END +
     CASE WHEN Humid06Qual IS NOT NULL THEN 1 ELSE 0 END +
     CASE WHEN Humid09Qual IS NOT NULL THEN 1 ELSE 0 END +
     CASE WHEN Humid12Qual IS NOT NULL THEN 1 ELSE 0 END +
     CASE WHEN Humid15Qual IS NOT NULL THEN 1 ELSE 0 END +
     CASE WHEN Humid18Qual IS NOT NULL THEN 1 ELSE 0 END +
     CASE WHEN Humid21Qual IS NOT NULL THEN 1 ELSE 0 END),
    0
  ) AS AvgHumidQual, 
t2.sunshinequal,
(
    COALESCE(Okta00Qual, 0) + COALESCE(Okta03Qual, 0) + COALESCE(Okta06Qual, 0) + COALESCE(Okta09Qual, 0) + 
    COALESCE(Okta12Qual, 0) + COALESCE(Okta15Qual, 0) + COALESCE(Okta18Qual, 0) + COALESCE(Okta21Qual, 0)
  ) / 
  NULLIF(
    (CASE WHEN Okta00Qual IS NOT NULL THEN 1 ELSE 0 END +
     CASE WHEN Okta03Qual IS NOT NULL THEN 1 ELSE 0 END +
     CASE WHEN Okta06Qual IS NOT NULL THEN 1 ELSE 0 END +
     CASE WHEN Okta09Qual IS NOT NULL THEN 1 ELSE 0 END +
     CASE WHEN Okta12Qual IS NOT NULL THEN 1 ELSE 0 END +
     CASE WHEN Okta15Qual IS NOT NULL THEN 1 ELSE 0 END +
     CASE WHEN Okta18Qual IS NOT NULL THEN 1 ELSE 0 END +
     CASE WHEN Okta21Qual IS NOT NULL THEN 1 ELSE 0 END),
    0
  ) AS AvgOktaQual
FROM sites as t1 
JOIN weather_data as t2
ON t1.site = t2.location
WHERE t2.dmy = ?
AND t1.lat BETWEEN ? AND ?
AND t1.state IN ({});
    '''.format(placeholders)

    print(query, 'QUERY')
    cursor.execute(query, (formatted_date, lat_min, lat_max, *states))
    results = cursor.fetchall()
    print(f"Query results: {results}")
    print(f"formatted_date, lat_min, lat_max: {formatted_date}, {lat_min}, {lat_max}")
    conn.close()

    # If validation passes, create results section
    lat_min_val = float(lat_min)
    lat_max_val = float(lat_max)

    # Create dynamic column headers based on selected metrics
    column_headers = ["Site No.", "Name", "Latitude", "Longitude"]
    metric_indices = []
    if 'precipitation' in metrics:
        column_headers.append("Precipitation")
        metric_indices.append(4)
    if 'evaporation' in metrics:
        column_headers.append("Evaporation")
        metric_indices.append(5)
    if 'temperature' in metrics:
        column_headers.append("Min Temp")
        column_headers.append("Max Temp")
        metric_indices.extend([6, 7])
    if 'humidity' in metrics:
        column_headers.append("Avg Humidity")
        metric_indices.append(8)
    if 'sunshine' in metrics:
        column_headers.append("Sunshine")
        metric_indices.append(9)
    if 'okta' in metrics:
        column_headers.append("Avg Okta")
        metric_indices.append(10)

    print(column_headers, 'COLLLLLLLLLLLLLLLLLLL')
    print(metric_indices, 'METRIC INDICES')
    print(states, 'STATES')

    success_message = f"""
    <div class="success-message" style="background-color: #e8f5e8; border: 1px solid #4caf50; 
        padding: 15px; margin: 20px; border-radius: 4px;">
        <h3 style="color: #2e7d32; margin-top: 0;">Search Parameters</h3>
        <p style="color: #2e7d32;">Latitude range: {lat_min_val}° to {lat_max_val}°</p>
        <p style="color: #2e7d32;">Selected metrics: {', '.join(metrics)}</p>
        <p style="color: #2e7d32;">Selected Date: {start_date_value}</p>
    </div>
    """

    if results:
        results_section = f"""
        <header class="white-dashboard">
            <ul class="dashboard-list">
                {''.join(f'<li>{header}</li>' for header in column_headers)}
            </ul>
        </header>
        <hr>
        """
        for row in results:
            row_html = [f"<li>{row[0]}</li>", f"<li>{row[1]}</li>", f"<li>{row[2]}</li>", f"<li>{row[3]}</li>"]
            for idx in metric_indices:
                row_html.append(f"<li>{row[idx] if str(row[idx]).strip() else 'N/A'}</li>")
            results_section += f"""
            <header class=\"results-description2\">
                <ul class=\"entries-list\">
                    {''.join(row_html)}
                </ul>
            </header>
            <hr>
            """
    else:
        results_section = "<div class='error-container' style='padding: 15px;'>No results found for the selected criteria.</div>"

    return base_page_html.format(
        lat_min_value=lat_min_value,
        lat_max_value=lat_max_value,
        start_date_value=start_date_value,
        precipitation_checked=precipitation_checked_value,
        evaporation_checked=evaporation_checked_value,
        temp_checked=temp_checked_value,
        humidity_checked=humidity_checked_value,
        sunshine_checked=sunshine_checked_value,
        okta_checked=okta_checked_value,
        qld_checked=qld_checked_value,
        aet_checked=aet_checked_value,
        aat_checked=aat_checked_value,
        nsw_checked=nsw_checked_value,
        sa_checked=sa_checked_value,
        nt_checked=nt_checked_value,
        wa_checked=wa_checked_value,
        tas_checked=tas_checked_value,
        vic_checked=vic_checked_value,
        error_message=error_message,
        success_message=success_message,
        results_section=results_section,
    )
