using System;
using System.Collections;
using System.Collections.Generic;

namespace StudentGrades
{
    internal class Program
    {
        // Hashtable to store student ID
        private Hashtable grades;

        // initialize the grades hashtable
        public Program()
        {
            grades = new Hashtable();
        }

        // add new student
        public void newStudent(int studentID)
        {
            if (!grades.ContainsKey(studentID))
            {
                //add new student kapag wala pa sa list yung studentID
                grades.Add(studentID, new List<int>());
            }
        }

        //  add grades for a student
        public void addGrades(int studentID, List<int> newGrades)
        {
            if (grades.ContainsKey(studentID))
            {
                // retrieve the list of grades and add new grades kapag nasa list yung studentID
                List<int> studentGrades = (List<int>)grades[studentID];
                studentGrades.AddRange(newGrades);
            }
            else
            {
                Console.WriteLine("Student ID not found!");
            }
        }

        // calculate the average grade of a student
        public void average(int studentID)
        {
            double sum = 0;

            if (grades.ContainsKey(studentID))
            {
                //  retrieve the list of grades for the student kapag nasa list yung studentID
                List<int> studentGrades = (List<int>)grades[studentID];

                if (studentGrades.Count == 0)
                {
                    // error message kapag walang laman yung grade
                    Console.WriteLine("No grades on the list");
                }
                else
                {
                    // kapag meron add niya lahat ng grade
                    foreach (int grade in studentGrades)
                    {
                        sum += grade;
                    }
                }

                // Calculate and display the average grade
                double average = sum / grades.Count;
                Console.WriteLine("Average grade of student " + studentID + ": " + average);
            }
            else
            {
                Console.WriteLine("Student ID not found!");
            }
        }

        // display grades of a student
        public void displayGrades(int studentID)
        {
            if (grades.ContainsKey(studentID))
            {
                //  retrieve the list of grades and display yung grades kapag meron sa list yung studentID
                List<int> studentGrades = (List<int>)grades[studentID];
                Console.Write("Grades of student " + studentID + ": ");
                foreach (int grade in studentGrades)
                {
                    Console.Write(grade + " ");
                }
                Console.WriteLine(); // next line after printing grades
            }
            else
            {
                Console.WriteLine("Student ID not found!");
            }
        }
        
        public static void Main(string[] args)
        {
            // instance of the Program class
            Program studentGrades = new Program();

            // Adding a new student (ID: 1) and adding grades for that student
            studentGrades.newStudent(1);
            studentGrades.addGrades(1, new List<int> { 90, 85, 88 });

            // Displaying grades and average for student 1
            studentGrades.displayGrades(1);
            studentGrades.average(1);

            // Adding a new student (ID: 2) and adding grades for that student
            studentGrades.newStudent(2);
            studentGrades.addGrades(2, new List<int> { 78, 82, 75 });

            // Displaying grades and average for student 2
            studentGrades.displayGrades(2);
            studentGrades.average(2);

            Console.ReadLine(); 
        }
    }
}
