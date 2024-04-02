

function Main() {

	return (
		<div className="Main">
      <div className="Main_head">
          <div className="head_text">Your Current Dashboard for today</div>
          <div className="calender"><input type="date"></input></div>
      </div>
      <div className="total">
          <div className="total_size">
              <div className="t_ship_logo"><div class="t_ship_logo2"></div></div>
              <div className="t_ship">
                  <div className="t_ship_text">Total Shipment</div>
                  <div className="t_ship_value">45</div>
              </div>
          </div>
          <div className="total_size">
              <div className="t_ship_logo"><div class="t_ship_logo3"></div></div>
              <div className="t_ship">
                  <div className="t_ship_text">Total Order</div>
                  <div className="t_ship_value">80</div>
              </div>
          </div>
          <div className="total_size">
              <div className="t_ship_logo"><div class="t_ship_logo4"></div></div>
              <div className="t_ship">
                  <div className="t_ship_text">Pending Order</div>
                  <div className="t_ship_value">35</div>
              </div>
          </div>
          <div className="total_size">
              <div className="t_ship_logo"><div class="t_ship_logo5"></div></div>
              <div className="t_ship">
                  <div className="t_ship_text">Total Revenue</div>
                  <div className="t_ship_value">N100,000</div>
              </div>
          </div>
      </div>
      <div className="ship_stat">
          <div className="ship_text">
              <div className="ship_text1">Shipment Statistics</div>
              <div className="ship_text2"><a href="{}">View all</a></div>
          </div>
          <div className="ship_head">
              <p>Order ID</p>
              <p>Vendor/Source</p>
              <p>Destination</p>
              <p>Departure Date</p>
              <p>Status</p>
              <p>Cost</p>
          </div>
          <div className="ship_others">
              <p>#142376</p>
              <p>Ocean Fright</p>
              <p>Lagos</p>
              <p>09/03/2024</p>
              <p>Pending</p>
              <p>N3000</p>
          </div>
          <div className="ship_others">
              <p>#142376</p>
              <p>Ocean Fright</p>
              <p>Lagos</p>
              <p>09/03/2024</p>
              <p>Pending</p>
              <p>N3000</p>
          </div>
          <div className="ship_others">
              <p>#142376</p>
              <p>Ocean Fright</p>
              <p>Lagos</p>
              <p>09/03/2024</p>
              <p>Pending</p>
              <p>N3000</p>
          </div>
          <div className="ship_others">
              <p>#142376</p>
              <p>Ocean Fright</p>
              <p>Lagos</p>
              <p>09/03/2024</p>
              <p>Pending</p>
              <p>N3000</p>
          </div>
          <div className="ship_others">
              <p>#142376</p>
              <p>Ocean Fright</p>
              <p>Lagos</p>
              <p>09/03/2024</p>
              <p>Pending</p>
              <p>N3000</p>
          </div>
      </div>
      <div className="geo">
          <div className="geo_head"><p>Geo Distribution - Lagos</p></div>
          <div className="geo_map"></div>
          <div className="geo_p_bar">
            <div className="geo_p_bar_text">Banana Island</div>
            <div className="geo_p_bar_text">Banana Island</div>
            <div className="geo_p_bar_text">Banana Island</div>
          </div>
          <div className="geo_p_bar">
              <div className="p_bar"><div className="p_bar_l pb1" style={{"--width": 40}} data-label="."></div><div><p>40%</p></div></div>
              <div className="p_bar"><div className="p_bar_l pb1" style={{"--width": 40}} data-label="."></div><div><p>40%</p></div></div>
              <div className="p_bar"><div className="p_bar_l pb1" style={{"--width": 40}} data-label="."></div><div><p>40%</p></div></div>
          </div>
          <div className="geo_p_bar">
            <div className="geo_p_bar_text">Banana Island</div>
            <div className="geo_p_bar_text">Banana Island</div>
            <div className="geo_p_bar_text">Banana Island</div>
          </div>
          <div className="geo_p_bar">
              <div className="p_bar"><div className="p_bar_l pb1" style={{"--width": 40}} data-label="."></div><div><p>40%</p></div></div>
              <div className="p_bar"><div className="p_bar_l pb1" style={{"--width": 40}} data-label="."></div><div><p>40%</p></div></div>
              <div className="p_bar"><div className="p_bar_l pb1" style={{"--width": 40}} data-label="."></div><div><p>40%</p></div></div>
          </div>
      </div>
    </div>
		);
}


export default Main;