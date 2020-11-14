import Head from 'next/head'
import Form from '../components/form';

export default () => (
  <div className="container">
    <Head>
      <title> YouTube Tools </title>
      <link rel="icon" href="/favicon.ico" />
    </Head>
    <header>
      {"will be header :)))))))))))))))))))))"}
    </header>
    <main>
      <Form />
    </main>
    <footer>
      {"will be footer :)))))))))))))))))))))"}
    </footer>
    <style jsx>{`
        .container {
          min-height: 100vh;
          padding: 0 0.5rem;
          display: flex;
          flex-direction: column;
          justify-content: center;
          align-items: center;
        }

        main {
          padding: 5rem 0;
          flex: 1;
          display: flex;
          flex-direction: column;
          justify-content: center;
          align-items: center;
        }

        header, footer {
          width: 100%;
          height: 70px;
          border-top: 1px solid #eaeaea;
          display: flex;
          justify-content: center;
          align-items: center;
        }

        header {
          border-bottom: 1px solid #eaeaea;
        }

        footer {
          border-top: 1px solid #eaeaea;
        }
      `}</style>

    <style jsx global>{`
        html,
        body {
          padding: 0;
          margin: 0;
        }

        * {
          box-sizing: border-box;
        }
      `}</style>
  </div>
)
