import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-fit-component',
  templateUrl: './fit-component.component.html',
  styleUrls: ['./fit-component.component.css']
})
export class FitComponentComponent implements OnInit {
  stepsEntries: any[] = [];
  caloriesEntries: any[] = [];

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.fetchData();
  }

  fetchData() {
    const stepsUrl = 'http://localhost:8000/getSteps';
    const caloriesUrl = 'http://localhost:8000/getCalories';
      
    this.http.get(stepsUrl).subscribe((stepsResponse: any) => {
      console.log('Steps data received successfully:', stepsResponse);
      this.stepsEntries = this.parseResponse(stepsResponse);
    }, error => {
      console.error('Error getting steps data:', error);
    });

    this.http.get(caloriesUrl).subscribe((caloriesResponse: any) => {
      console.log('Calories data received successfully:', caloriesResponse);
      this.caloriesEntries = this.parseResponse(caloriesResponse);
    }, error => {
      console.error('Error getting calories data:', error);
    });
  }

  parseResponse(response: any): any[] {
    const entries: any[] = [];
    for (const date in response) {
      if (response.hasOwnProperty(date)) {
        entries.push({ date, value: response[date].value });
      }
    }
    return entries;
  }
}
