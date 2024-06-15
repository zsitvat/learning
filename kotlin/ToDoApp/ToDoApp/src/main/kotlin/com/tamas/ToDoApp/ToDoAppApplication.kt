package com.tamas.ToDoApp

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication
import org.springframework.data.jpa.repository.config.EnableJpaRepositories

@SpringBootApplication
class ToDoAppApplication

fun main(args: Array<String>) {
	runApplication<ToDoAppApplication>(*args)
}
