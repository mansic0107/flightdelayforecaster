# Flight Delay Forecaster
  Using Flask Framework and raw data set for Python

<h2>How to Use</h2>
  
  <h3>Setting up Modules and Keys</h3>
 <ul>
 <li>Install Flask by typing the following command on terminal - sudo pip3 install flask</li>
 <li>Install json by typing the following command on terminal - sudo pip3 install json</li>
 </ul>
 
 <h3>Running the application</h3>
 <ul>
 <li>Run the python script flightweb.py</li>
 <li>Take any valid flight no from csv file 6.csv</li>
 <li>Now open - http://localhost:5000 on your browser</li>
 <li>The application is displayed.</li>
 <li>Enter the flight no and date</li>
 </ul>
 
 <h3>Description of the output</h3>
 <ul>
 <li>If the delay is less than 10 minutes then app will show no delay</li>
 <li>Otherwise the predicted delay will be shown as output</li>
 <li>Data set is trained such that flight delays are more on weekends than weekdays</li>

 </ul>
 
