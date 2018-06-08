//For sizes of internal referrer sticky ads

if (typeof internalReferralAdsCheck != 'undefined' && internalReferralAdsCheck ){
	
}else if(document.referrer.indexOf(location.protocol + "//" + location.host) === 0){
	var internalReferralAdsCheck = 1;
	
	var staticSizesEboundDynamicAdsDesktop = ["970x300"];
	var staticSizesEboundDynamicAdsTablet = ["336x280"];
	var staticSizesEboundDynamicAdsMobile = ["336x280"];
	//Ads Style for internal referrer ads only
	document.write('\
	<style>	\
	#ebound_internal_sticky_new_ads {	\
		visibility: hidden;\
		transition: 0.5s all;\
		transform: translateY(100%);\
		background: rgba(0,0,0,0.5);\
		height: 115px;\
		width: 100%;\
		z-index: 999;\
		position: fixed;\
		bottom: -150px;\
		right: 0;\
		left: 0;\
		margin: auto;\
	} 	\
	.show_ebound_internal_sticky {\
		visibility: visible !important;\
		transform: translateY(0) !important;\
	}\
	\
	.eboundClose {\
		float: left;\
		font-size: 21px;\
		font-weight: 700;\
		line-height: 1;\
		color: #000;\
		text-shadow: 0 1px 0 #fff;\
		filter: alpha(opacity=20);\
		opacity: .2;\
	}\
	\
	.eboundClose:focus, .eboundClose:hover {\
		color: #000;\
		text-decoration: none;\
		cursor: pointer;\
		filter: alpha(opacity=50);\
		opacity: .5;\
	}\
	\
	#ebound_internal_sticky_new_ads.ebound_internal_sticky_new_ads_mobile {\
		background:rgba(0,0,0,0.5);\
		height: 100%;\
	}\
	\
	.ebound_internal_sticky_new_ads_mobile #eboundInternalReferralAds {\
		top: 50% !important;\
		margin-top: -142px !important;\
		bottom: initial !important;\
	}\
	</style>');

	//Div area for internal referrer ads only

	document.write('<div id="ebound_internal_sticky_new_ads">\
		<div id="eboundInternalReferralAds" style="max-width: fit-content;\
		text-align: center;\
		background: #EEEEEE;\
		position: absolute;\
		bottom: 10px;\
		box-shadow: 0px 3px 19px -2px rgba(0,0,0,0.33);\
		left: 0;\
		right: 0;\
		margin: auto;">');

	//Loading ads
	document.write("<scr"+"ipt src='//publisher.eboundservices.com/dynamicAds/staticScript.js'></scr"+"ipt>"); 

	//Close button
	document.write('<button onclick="removeAdsReferralBanner()" style="background: none; border: 0; outline: none; position: absolute;top: -30px;left: -30px; opacity: 1;" class="eboundClose"> <img style="background: #eee;padding: 2px;border-radius: 50%;" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAnFBMVEUAAADVACvXACjXACjYACfYACfYACfTACzYACfYACfYACfYACfYACfYACfZACbYACfSAC3YACfYACfZACbbACTXACjYACfYACffACDXACj/AADYACfYACfYACf/AADZACbXACjYACfVACvRAC7YACfZACbXACjXACjMADPZACbYACfYACfYACfYACfYACfMADPXACjZACbYACcAAAA/WvaQAAAAMnRSTlMABkaUwNnzF/L23IL055lOEcXscgct47IQhwKIte4BNnnDDAvCn8FTChS/977dvQUzNW2ZHpoAAAABYktHRACIBR1IAAAACXBIWXMAAA3XAAAN1wFCKJt4AAAAB3RJTUUH4QMDDB45xof5CgAAAUtJREFUOMuFU9mWgjAUK1AWBRcQUXFBBBUVmZn8/8dNy9aCntO+FJo0N3cpIf3SdIOalmVSQ9fI57INB8BkOp2wzTHsEay5HmbzxZJ/LxfzGTx3oGL7CFah+A9XAXxJZB1hsx1KbjeI1v39CLt47CneIWo1NB/7L67JHn7jw8Uh/kaID3DrAN6Rmz8lssnkxNM5ejyIgTM/S5BeOvySIuH7GQZz4ARZfSlFnjV4liOt5bLA0YiOa3stx61mZDfkrdgVOotwb4UZQAtCCtoS2bqzGBSPLnRG8SyKJ2iHkwcoMV/CPAPLkpHEycsk1ltKvSiBUsLJ2/okVCPCKERVDhgsxNBkxU0KBjc5SLNq0uwZPE25UA3QErtCSaXujlmpq5++1KJZIjRr1m/fLNFuaUrDPyLarRwY9cgph1Y99uqHo356RPl4a5Wvz/8f5xQsQOAAu8gAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTctMDMtMDNUMTI6MzA6NTcrMDE6MDDEdDZnAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE3LTAzLTAzVDEyOjMwOjU3KzAxOjAwtSmO2wAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAASUVORK5CYII=" alt="close"><span style="color: #FFF;text-shadow: none;font-weight: 400;font-size: 10px;padding-right: 5px;">CLOSE</span> </button>\
			\
		</div>\
		\
	</div>\
	');
	// console.log(document.querySelectorAll('#eboundInternalReferralAds ins')[0].dataset.adSlot);
	// document.querySelectorAll('#eboundInternalReferralAds ins')[0].dataset.adSlot = "7056164043";

	//On ready function don't display ads if the following conditions don't meet
	function eboundReady(fn){var d=document;(d.readyState=='loading')?d.addEventListener('DOMContentLoaded',fn):fn();}
	eboundReady(function(){
		// Your code to run since DOM is loaded and ready
		
		if(document.referrer.indexOf(location.protocol + "//" + location.host) === 0){
			var d = document.getElementById("ebound_internal_sticky_new_ads");
			ebCheckCookie();
			var run = true;
			if( eboundMD.mobile() || eboundMD.tablet() ){
				console.log(Number(ebGetCookie("eboundInternalReferralAds")));
				
				document.querySelectorAll('#eboundInternalReferralAds ins')[0].dataset.adSlot = "9207203102";
				console.log(document.querySelectorAll('#eboundInternalReferralAds ins')[0].dataset.adSlot);
		
				if( Number(ebGetCookie("eboundInternalReferralAds")) === 0 || ebGetCookie("eboundInternalReferralAds") > 3){
					ebSetCookie("eboundInternalReferralAds", Number(1), -1);
					ebSetCookie("eboundInternalReferralAds", Number(1), 1);
					run = true;
					d.className += "ebound_internal_sticky_new_ads_mobile";			
				}else if(ebGetCookie("eboundInternalReferralAds") <= 3){
					run = false;
				}
			}else{
				document.querySelectorAll('#eboundInternalReferralAds ins')[0].dataset.adSlot = "4939744013";
				console.log(document.querySelectorAll('#eboundInternalReferralAds ins')[0].dataset.adSlot);
		
			}
				
			if(run){
				
				d.className += " show_ebound_internal_sticky";			
				setTimeout(function(){
					var d = document.getElementById("ebound_internal_sticky_new_ads");
					d.style.bottom='0';
					
				}, 300);
			}else{
				removeAdsReferralBanner();
			}
		}else{
			removeAdsReferralBanner();
		}
		
	});

} //If condition check

//Remove the ads on close button
function removeAdsReferralBanner(){
	var d = document.getElementById("ebound_internal_sticky_new_ads");
	d.parentNode.removeChild(d)
	// d.innerHTML = '';
	// d.className = "";
}

//Cookies for mobile ads
function ebSetCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    var expires = "expires="+d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function ebGetCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

function ebCheckCookie() {
    var eboundInternalReferralAds=ebGetCookie("eboundInternalReferralAds");
    if (eboundInternalReferralAds != "") {
       ebSetCookie("eboundInternalReferralAds", (Number(1)+Number(eboundInternalReferralAds)), 1);
    } else {
       ebSetCookie("eboundInternalReferralAds", Number(0), 1);
    }
}
