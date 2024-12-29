import { NextResponse } from 'next/server'
import { PrismaClient } from '@prisma/client'

const prisma = new PrismaClient()

export async function GET() {
  const todos = await prisma.todo.findMany()
  return NextResponse.json(todos)
}

export async function POST(request: Request) {
  const data = await request.json()
  const todo = await prisma.todo.create({
    data: {
      text: data.text,
      category: data.category,
      priority: data.priority,
    },
  })
  return NextResponse.json(todo)
}

