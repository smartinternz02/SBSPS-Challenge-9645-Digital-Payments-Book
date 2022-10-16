import React from 'react'
import Layout from './Layout'
import HomeCard from './components/homeCards'
function Home() {
  return (
    <Layout pageName={'Wellcome to Mercurius Book'} pageDesc={'We are glad to invite you to the future of Digital Payment Books'}>
      <HomeCard></HomeCard>
    </Layout>
  )
}

export default Home