import type { ReactElement } from 'react'
import Layout from '@/src/components/admin/Layout'
import type { NextPageWithLayout } from '@/src/pages/_app'
import Home from '@/src/components/Home'

const Page: NextPageWithLayout = () => {
  return <Home/>
}

Page.getLayout = function getLayout(page: ReactElement) {
  return (
    <Layout>
      {page}
    </Layout>
  )
}

export default Page