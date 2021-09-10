import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

import '../node_modules/swiper/swiper.min.css';
import '../node_modules/swiper/components/navigation/navigation.min.css';
import '../node_modules/swiper/components/pagination/pagination.min.css';
import '../node_modules/swiper/components/scrollbar/scrollbar.min.css';

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
