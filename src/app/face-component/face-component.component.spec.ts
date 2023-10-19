import { TestBed } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { FaceComponentComponent } from './face-component.component';

describe('FaceComponentComponent', () => {
  beforeEach(() => TestBed.configureTestingModule({
    imports: [RouterTestingModule],
    declarations: [FaceComponentComponent]
  }));

  it('should create the app', () => {
    const fixture = TestBed.createComponent(FaceComponentComponent);
    const app = fixture.componentInstance;
    expect(app).toBeTruthy();
  });

  it(`should have as title 'pwa-practice'`, () => {
    const fixture = TestBed.createComponent(FaceComponentComponent);
    const app = fixture.componentInstance;
    expect(app.title).toEqual('pwa-practice');
  });

  it('should render title', () => {
    const fixture = TestBed.createComponent(FaceComponentComponent);
    fixture.detectChanges();
    const compiled = fixture.nativeElement as HTMLElement;
    expect(compiled.querySelector('.content span')?.textContent).toContain('pwa-practice app is running!');
  });
});
