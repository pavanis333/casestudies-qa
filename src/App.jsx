import { useState, useEffect, useMemo } from 'react'
import data from './data.json'
import './App.css'

function App() {
  const [activeTab, setActiveTab] = useState('library')
  const [selectedCase, setSelectedCase] = useState(null)
  const [searchQuery, setSearchQuery] = useState('')
  const [revealedAnswers, setRevealedAnswers] = useState({})
  const [progress, setProgress] = useState(() => {
    const saved = localStorage.getItem('upsc_progress')
    return saved ? JSON.parse(saved) : {}
  })
  const [favorites, setFavorites] = useState(() => {
    const saved = localStorage.getItem('upsc_favorites')
    return saved ? JSON.parse(saved) : []
  })

  // Flashcard state
  const [currentFlashcard, setCurrentFlashcard] = useState(null)
  const [isFlipped, setIsFlipped] = useState(false)

  useEffect(() => {
    localStorage.setItem('upsc_progress', JSON.stringify(progress))
  }, [progress])

  useEffect(() => {
    localStorage.setItem('upsc_favorites', JSON.stringify(favorites))
  }, [favorites])

  const [selectedYear, setSelectedYear] = useState('All')
  const [selectedCategory, setSelectedCategory] = useState('All')
  const [showSettings, setShowSettings] = useState(false)

  // Extract unique years and categories
  const years = useMemo(() => ['All', ...new Set(data.map(d => d.year))].sort((a, b) => b - a), [])
  const categories = useMemo(() => ['All', ...new Set(data.map(d => d.category))].sort(), [])

  useEffect(() => {
    localStorage.setItem('upsc_progress', JSON.stringify(progress))
  }, [progress])

  useEffect(() => {
    localStorage.setItem('upsc_favorites', JSON.stringify(favorites))
  }, [favorites])

  const exportData = () => {
    const data = {
      progress: JSON.parse(localStorage.getItem('upsc_progress') || '{}'),
      favorites: JSON.parse(localStorage.getItem('upsc_favorites') || '[]')
    }
    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `upsc-ethics-progress-${new Date().toISOString().split('T')[0]}.json`
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)
    URL.revokeObjectURL(url)
  }

  const importData = (event) => {
    const file = event.target.files[0]
    if (!file) return

    const reader = new FileReader()
    reader.onload = (e) => {
      try {
        const parsed = JSON.parse(e.target.result)
        if (parsed.progress && parsed.favorites) {
          if (confirm('This will overwrite your current progress. Continue?')) {
            setProgress(parsed.progress)
            setFavorites(parsed.favorites)
            setShowSettings(false)
            alert('Data imported successfully!')
          }
        } else {
          alert('Invalid data file format.')
        }
      } catch (err) {
        alert('Error parsing file.')
      }
    }
    reader.readAsText(file)
  }

  const caseStudies = useMemo(() => {
    let filtered = data

    if (selectedYear !== 'All') {
      filtered = filtered.filter(cs => cs.year === parseInt(selectedYear) || cs.year === selectedYear)
    }

    if (selectedCategory !== 'All') {
      filtered = filtered.filter(cs => cs.category === selectedCategory)
    }

    if (searchQuery) {
      const query = searchQuery.toLowerCase()
      filtered = filtered.filter(cs =>
        cs.title.toLowerCase().includes(query) ||
        cs.category.toLowerCase().includes(query) ||
        cs.scenario.toLowerCase().includes(query)
      )
    }
    return filtered
  }, [searchQuery, selectedYear, selectedCategory])

  const highlightText = (text, query) => {
    if (!query) return text
    const parts = text.split(new RegExp(`(${query})`, 'gi'))
    return parts.map((part, i) =>
      part.toLowerCase() === query.toLowerCase() ? <mark key={i}>{part}</mark> : part
    )
  }

  useEffect(() => {
    if (activeTab === 'flashcards') {
      generateRandomFlashcard()
    }
  }, [activeTab])

  const generateRandomFlashcard = () => {
    const randomCase = data[Math.floor(Math.random() * data.length)]
    const randomDilemma = randomCase.dilemmas[Math.floor(Math.random() * randomCase.dilemmas.length)]
    setCurrentFlashcard({
      id: randomCase.id,
      front: randomDilemma,
      back: `Case: ${randomCase.title} (${randomCase.year})`,
      category: randomCase.category
    })
    setIsFlipped(false)
  }

  const toggleReveal = (questionId) => {
    setRevealedAnswers(prev => ({
      ...prev,
      [questionId]: !prev[questionId]
    }))
  }

  const toggleFavorite = (e, id) => {
    e.stopPropagation()
    setFavorites(prev =>
      prev.includes(id) ? prev.filter(f => f !== id) : [...prev, id]
    )
  }

  const markProgress = (id, type) => {
    setProgress(prev => ({
      ...prev,
      [id]: { ...prev[id], [type]: true }
    }))
  }

  const openCase = (cs) => {
    setSelectedCase(cs)
    setRevealedAnswers({})
    markProgress(cs.id, 'read')
  }

  const resetProgress = () => {
    if (confirm('Are you sure you want to reset all your progress? This cannot be undone.')) {
      setProgress({})
      setFavorites([])
    }
  }

  const getProgressStats = () => {
    const total = data.length
    const read = Object.values(progress).filter(p => p.read).length
    const practiced = Object.values(progress).filter(p => p.practiced).length
    return { total, read, practiced }
  }

  const stats = getProgressStats()

  return (
    <div className="app-container">
      <nav className="app-navbar glass">
        <div className="logo-text">
          <span>🏛️</span> UPSC Ethics Hub
        </div>
        <div className="nav-links">
          <div
            className={`nav-link ${activeTab === 'library' ? 'active' : ''}`}
            onClick={() => setActiveTab('library')}
          >
            Library
          </div>
          <div
            className={`nav-link ${activeTab === 'practice' ? 'active' : ''}`}
            onClick={() => setActiveTab('practice')}
          >
            Practice
          </div>
          <div
            className={`nav-link ${activeTab === 'flashcards' ? 'active' : ''}`}
            onClick={() => setActiveTab('flashcards')}
          >
            Flashcards
          </div>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
          <div className="stats-badge">
            {stats.read}/{stats.total} Cases Read
          </div>
          <button
            onClick={() => setShowSettings(true)}
            style={{
              background: 'none',
              border: 'none',
              fontSize: '1.5rem',
              cursor: 'pointer',
              padding: '0.2rem'
            }}
            title="Settings"
          >
            ⚙️
          </button>
        </div>
      </nav>

      <main className="container animate-fade-in">
        <header className="dashboard-header">
          <h1 className="title-gradient">
            {activeTab === 'library' && 'Case Study Library'}
            {activeTab === 'practice' && 'Practice Scenarios'}
            {activeTab === 'flashcards' && 'Ethics Flashcards'}
          </h1>
          <p className="case-year" style={{ fontSize: '1.1rem', marginTop: '0.5rem' }}>
            {activeTab === 'flashcards'
              ? 'Test your ethical intuition with quick dilemma recall.'
              : 'Master GS Paper IV with real UPSC case studies and model answers.'}
          </p>

          {activeTab !== 'flashcards' && (
            <div className="search-container">
              <div className="filters">
                <select
                  value={selectedYear}
                  onChange={(e) => setSelectedYear(e.target.value)}
                  className="filter-select"
                >
                  {years.map(y => <option key={y} value={y}>{y === 'All' ? 'All Years' : y}</option>)}
                </select>
                <select
                  value={selectedCategory}
                  onChange={(e) => setSelectedCategory(e.target.value)}
                  className="filter-select"
                >
                  {categories.map(c => <option key={c} value={c}>{c === 'All' ? 'All Categories' : c}</option>)}
                </select>
              </div>
              <div style={{ position: 'relative', flex: 1 }}>
                <input
                  type="text"
                  className="search-bar"
                  placeholder="Search by title, category, or ethics keywords..."
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                />
                {searchQuery && (
                  <button
                    style={{ position: 'absolute', right: '1.5rem', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }}
                    onClick={() => setSearchQuery('')}
                  >
                    Clear
                  </button>
                )}
              </div>
            </div>
          )}
        </header>

        {(activeTab === 'library' || activeTab === 'practice') && (
          <div className="case-grid">
            {caseStudies.length === 0 ? (
              <div className="no-results">
                <h3>No cases found</h3>
                <p>Try adjusting your search or filters.</p>
                <button
                  className="btn-primary"
                  onClick={() => { setSearchQuery(''); setSelectedYear('All'); setSelectedCategory('All'); }}
                  style={{ marginTop: '1rem' }}
                >
                  Clear All Filters
                </button>
              </div>
            ) : (
              caseStudies.map(cs => (
                <div
                  key={cs.id}
                  className={`case-card ${progress[cs.id]?.read ? 'is-read' : ''}`}
                  onClick={() => openCase(cs)}
                >
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                    <span className="case-tag">{highlightText(cs.category, searchQuery)}</span>
                    <button
                      className={`fav-btn ${favorites.includes(cs.id) ? 'active' : ''}`}
                      onClick={(e) => toggleFavorite(e, cs.id)}
                    >
                      {favorites.includes(cs.id) ? '★' : '☆'}
                    </button>
                  </div>
                  <h2 className="case-title">{highlightText(cs.title, searchQuery)}</h2>
                  <p className="case-scenario-preview">{highlightText(cs.scenario, searchQuery)}</p>
                  <div className="case-footer">
                    <div className="case-year">
                      {cs.year} • #{cs.case_number}
                      {progress[cs.id]?.practiced && <span className="status-dot">✓ Practiced</span>}
                    </div>
                    <button className="btn-primary">
                      {activeTab === 'library' ? 'Analysis' : 'Practice'}
                    </button>
                  </div>
                </div>
              ))
            )}
          </div>
        )}

        {activeTab === 'flashcards' && currentFlashcard && (
          <div className="flashcard-container">
            <div className={`flashcard ${isFlipped ? 'flipped' : ''}`} onClick={() => setIsFlipped(!isFlipped)}>
              <div className="flashcard-inner">
                <div className="flashcard-front">
                  <span className="case-tag">{currentFlashcard.category}</span>
                  <h3>"{currentFlashcard.front}"</h3>
                  <p style={{ marginTop: '2rem', fontSize: '0.8rem', opacity: 0.6 }}>Click to see context</p>
                </div>
                <div className="flashcard-back">
                  <h3>{currentFlashcard.back}</h3>
                  <button
                    className="btn-primary"
                    style={{ marginTop: '2rem', background: 'white', color: 'var(--accent)' }}
                    onClick={(e) => { e.stopPropagation(); openCase(data.find(d => d.id === currentFlashcard.id)); }}
                  >
                    Go to Case Details
                  </button>
                </div>
              </div>
            </div>
            <button className="btn-primary" onClick={(e) => { e.stopPropagation(); generateRandomFlashcard(); }}>
              Next Flashcard
            </button>
          </div>
        )}
      </main>

      {/* Settings Modal */}
      {showSettings && (
        <div className="modal-overlay" onClick={() => setShowSettings(false)}>
          <div className="modal-content animate-fade-in" style={{ maxWidth: '500px' }} onClick={e => e.stopPropagation()}>
            <button className="close-btn" onClick={() => setShowSettings(false)}>×</button>
            <h2 style={{ marginBottom: '1.5rem' }}>Settings & Data</h2>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
              <button className="btn-primary" onClick={exportData} style={{ display: 'flex', justifyContent: 'center', gap: '0.5rem' }}>
                ⬇️ Export Progress Data
              </button>

              <label className="btn-primary" style={{ display: 'flex', justifyContent: 'center', gap: '0.5rem', cursor: 'pointer', background: 'var(--card-bg)', color: 'var(--text)', border: '1px solid var(--border)' }}>
                ⬆️ Import Progress Data
                <input type="file" accept=".json" onChange={importData} style={{ display: 'none' }} />
              </label>

              <hr style={{ margin: '1rem 0', borderColor: 'var(--border)' }} />

              <button
                onClick={resetProgress}
                style={{
                  background: '#ef4444',
                  color: 'white',
                  padding: '0.8rem',
                  borderRadius: '8px',
                  fontWeight: 600
                }}
              >
                Reset All Progress
              </button>
            </div>
            <p style={{ marginTop: '1.5rem', fontSize: '0.85rem', color: 'var(--text-muted)', textAlign: 'center' }}>
              Export your data to save a backup or transfer to another device.
            </p>
          </div>
        </div>
      )}

      {/* Case Detail Modal */}
      {selectedCase && (
        <div className="modal-overlay" onClick={() => setSelectedCase(null)}>
          <div className="modal-content animate-fade-in" onClick={e => e.stopPropagation()}>
            <button className="close-btn" onClick={() => setSelectedCase(null)}>×</button>
            <div style={{ display: 'flex', gap: '1rem', alignItems: 'center', marginBottom: '1rem' }}>
              <span className="case-tag">{selectedCase.category}</span>
              <span className="case-year">{selectedCase.year} • Case Study #{selectedCase.case_number}</span>
            </div>
            <h1 style={{ margin: '0.5rem 0 1.5rem', fontSize: '2rem' }}>{selectedCase.title}</h1>

            <div className="case-scenario" style={{ marginBottom: '2rem' }}>
              <h3 style={{ marginBottom: '0.75rem', color: 'var(--accent)' }}>The Situation</h3>
              <p style={{ fontSize: '1.1rem', background: 'rgba(59, 130, 246, 0.05)', padding: '1.5rem', borderRadius: 'var(--radius)', borderLeft: '4px solid var(--accent)' }}>
                {selectedCase.scenario}
              </p>
            </div>

            <h3 style={{ marginBottom: '0.75rem' }}>Fundamental Dilemmas</h3>
            <div className="dilemma-list">
              {selectedCase.dilemmas.map((d, i) => (
                <span key={i} className="dilemma-item">{d}</span>
              ))}
            </div>

            <div className="qa-section">
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem', borderBottom: '2px solid var(--border)', paddingBottom: '0.5rem' }}>
                <h3 style={{ margin: 0 }}>Answer Strategy</h3>
                {activeTab === 'practice' && !progress[selectedCase.id]?.practiced && (
                  <button
                    className="btn-primary"
                    style={{ fontSize: '0.75rem', padding: '0.4rem 0.8rem' }}
                    onClick={() => markProgress(selectedCase.id, 'practiced')}
                  >
                    Mark as Practiced
                  </button>
                )}
              </div>

              {selectedCase.questions.map((q, idx) => (
                <div key={q.id || idx} className="question-box">
                  <p className="question-text">Q{idx + 1}: {q.question}</p>

                  {activeTab === 'practice' ? (
                    <>
                      {revealedAnswers[q.id || idx] ? (
                        <div className="answer-text animate-fade-in">
                          <p style={{ whiteSpace: 'pre-line' }}>{q.answer}</p>
                          <button
                            className="reveal-btn"
                            style={{ display: 'block', marginTop: '1rem', background: 'var(--text-muted)' }}
                            onClick={() => toggleReveal(q.id || idx)}
                          >
                            Hide Answer
                          </button>
                        </div>
                      ) : (
                        <button className="btn-primary" onClick={() => toggleReveal(q.id || idx)}>
                          Show Model Thinking
                        </button>
                      )}
                    </>
                  ) : (
                    <div className="answer-text">
                      <p style={{ whiteSpace: 'pre-line' }}>{q.answer}</p>
                    </div>
                  )}
                </div>
              ))}
            </div>

            <div className="ethical-keywords" style={{ marginTop: '2rem', padding: '1.5rem', background: 'var(--bg)', borderRadius: 'var(--radius)' }}>
              <h4 style={{ marginBottom: '1rem' }}>💡 Pro-Tip: Key Ethical Terms for this Case</h4>
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.5rem' }}>
                {selectedCase.category === 'Crisis Management' && ['Emotional Intelligence', 'Public Trust Doctrine', 'Duty vs Responsibility'].map(t => <span key={t} className="keyword-tag">#{t}</span>)}
                {selectedCase.category === 'Environmental Ethics' && ['Inter-generational Equity', 'Sustainable Development', 'Precautionary Principle'].map(t => <span key={t} className="keyword-tag">#{t}</span>)}
                {/* Fallback tags */}
                {['Integrity', 'Social Contract', 'Accountability'].map(t => <span key={t} className="keyword-tag">#{t}</span>)}
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

export default App
