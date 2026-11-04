import './App.css'

export default function App() {
  return (
    <>
      <a className="skip" href="#main">Skip to content</a>
      <header><p>NASA Earth Information Jukebox project</p><h1>Monsoon Listener</h1></header>
      <main id="main">
        <h2>Listen to a changing Earth</h2>
        <p>Project foundation. NASA tracks and playback are being prepared.</p>
        <section aria-labelledby="tracks"><h2 id="tracks">Planned tracks</h2>
          <article><h3>Rainfall across Pakistan</h3><p>First release: explore rainfall patterns, compare regions and inspect the evidence.</p><p><strong>Status:</strong> Source validation pending</p></article>
          <article><h3>Ocean Duet</h3><p>Extension: compare ocean surface temperature with a documented reference.</p><p><strong>Status:</strong> Planned after the rainfall release passes its checks</p></article>
        </section>
        <p>No scientific observations or playable NASA tracks are included in this scaffold.</p>
      </main>
    </>
  )
}
