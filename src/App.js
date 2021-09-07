// import { useState, useEffect } from 'react';

import '../node_modules/swiper/swiper.min.css';
import '../node_modules/swiper/components/navigation/navigation.min.css';
import '../node_modules/swiper/components/pagination/pagination.min.css';
import '../node_modules/swiper/components/scrollbar/scrollbar.min.css';

import Content from './components/Content';
import Footer from './components/Footer'
import Header from './components/Header';
import Jumbotron from './components/Jumbotron';

function App() {
  return (
    <div className="App">
      <Header title="Rumah Film" />
      <div className="my-10 mx-10">
        <Jumbotron />
        <Content />
      </div>
      <Footer />
    </div>
  );
}

export default App;
