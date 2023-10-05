import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { WebcamImage, WebcamUtil } from 'ngx-webcam';
import { Observable, Subject } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  constructor(public http: HttpClient) {
    this.multipleWebcamsAvailable = false;
    this.trigger = new Subject <void>();
    this.personDetected = "";
  }

  public multipleWebcamsAvailable;
  private trigger: Subject<void>;
  public webcamImage: WebcamImage | undefined;
  public personDetected: string;
  
  public ngOnInit(): void {
    WebcamUtil.getAvailableVideoInputs()
      .then((mediaDevices: MediaDeviceInfo[]) => {
        this.multipleWebcamsAvailable = mediaDevices && mediaDevices.length > 1;
      });
  }

  public handleImage(webcamImage: WebcamImage): void {
    console.info('received webcam image', webcamImage);
    this.webcamImage = webcamImage;
  }

  public triggerSnapshot(): void {
    this.trigger.next();
  }

  public get triggerObservable(): Observable<void> {
    return this.trigger.asObservable();
  }

  public sendImage(event: Event) {
    event.preventDefault();
    const imageData = this.webcamImage ? this.webcamImage.imageAsDataUrl : null;

    console.log(imageData);
    
    if (imageData) {
      // Replace 'your-api-endpoint' with the actual API endpoint
      const apiUrl = 'http://localhost:8000/match';
      
      // Send a POST request to the API with the image data
      this.http.post(apiUrl, { imageData }).subscribe((response: any) => {
        // Handle the API response as needed
        console.log('Image data sent successfully:');
        this.personDetected = response?.name;
      }, error => {
        // Handle any errors
        console.error('Error sending image data:', error);
      });
    }
  }
  
  title = 'pwa-practice';
}