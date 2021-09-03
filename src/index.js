import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import '../node_modules/swiper/swiper-bundle.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

// import SwiperCore from 'swiper'
// import { Virtual } from 'swiper'
// import { Swiper } from 'swiper/swiper-bundle'

// import AppLogo from './media/rmlogos.png'
// import StarRatingLogo from './media/star-rating-sprite.png'

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
