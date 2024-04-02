function Sidebar() {
	return (<div className="sidebar">
                <div className="side_menu">
                    <div className="side_menu2">
	                    <div className="side_setting">
	                        <div className="dash_logo"></div>
	                        <div className="dash_text">Dashboard</div>
	                    </div>
	                    <div className="side_setting">
	                        <div className="order_logo"></div>
	                        <div className="dash_text">Orders</div>
	                    </div>
	                    <div className="side_setting">
	                        <div className="product_logo"></div>
	                        <div className="dash_text">Products</div>
	                    </div>
	                </div>
                </div>
                <div className="side_setting">
                    <div className="logout_logo"></div>
                    <div className="dash_text">Logout</div>
                </div>
            </div>
            );
}

export default Sidebar;