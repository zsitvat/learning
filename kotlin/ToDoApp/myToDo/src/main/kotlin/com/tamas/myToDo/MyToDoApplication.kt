package com.tamas.myToDo

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication
class MyToDoApplication

fun main(args: Array<String>) {
	runApplication<MyToDoApplication>(*args)
}