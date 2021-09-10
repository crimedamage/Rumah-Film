import React from 'react'

import Content from './components/Content';
import Footer from './components/Footer'
import Header from './components/Header';
import Jumbotron from './components/home/Jumbotron';

const Home = () => {
  return (
    <>
      <Header title="Rumah Film" />
      <div className="my-10 mx-10">
        <Jumbotron />
        <Content />
      </div>
      <Footer />
    </>
  )
}

export default Home
