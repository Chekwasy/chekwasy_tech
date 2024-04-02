
function Navbar() {
	return (<div className="nav">
            <div className="h_logo">
            </div>
            <div className="welcome">
                <div className="hand_logo"></div>
                <div className="greet">
                		<div className="hand_text white_text">Good Morning Yinka!,</div>
                    <div className="white_text productive_text">Let's get productive today!</div>
                </div>
            </div>
            <div class="menu">
                <div className="bell"><div class="bell_logo"></div></div>
                <div className="profile_pic"></div>
                <div className="user white_text" ><div class="username">Wittig</div><div class="admin">Admin</div></div>
            </div>
        </div>
        );
}


export default Navbar;