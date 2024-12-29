import { Navbar } from '@/components/Navbar'
import { AddTodo } from '@/components/AddTodo'
import { Dashboard } from '@/components/Dashboard'
import { Analytics } from '@/components/Analytics'
import { ErrorBoundary } from '@/components/ErrorBoundary'

export default function Home() {
  return (
    <div className="app-container">
      <ErrorBoundary>
        <Navbar />
        <main>
          <AddTodo />
          <Dashboard />
          <Analytics />
        </main>
      </ErrorBoundary>
    </div>
  )
}

