import React, { useRef } from "react";
import { Toast } from "primereact/toast";
import { Card } from "primereact/card";
import ClassificationComponent from "./components/ClassificationComponent";
import ImageUpload from "./components/ImageUpload";
import "./App.css"; // Import a CSS file for custom styles
import 'primeicons/primeicons.css';                        //icons
import "primereact/resources/themes/lara-light-cyan/theme.css";
import { RadioButton } from "primereact/radiobutton";
import { useState } from "react";
function App() {
  const toast = useRef(null);
  const [model, setModel] = useState('googlenet');

  return (
    <div className="container">
      <Toast ref={toast} />

      <div className="p-grid p-justify-center">
        <div className="p-col-12">
          <Card
            title="Face Emotion Detection"
            subTitle="Classify and analyze face emotion images"
            className="card"
          ></Card>
        </div>

        <div className="p-col-12 p-md-6 p-lg-6">
          <Card title="Upload Face Image" className="card">
            <div className="content">
              <ImageUpload toast={toast} />
            </div>

            <div style={{
              marginTop: '20px',
              display: 'flex',
              flexDirection: 'row',
              alignItems: 'flex-center',
              gap: '10px',
            }}>
              <div style={{ marginRight: '10px', marginLeft: "50px" }}>
                <span style={{ fontWeight: 'bold' }}>Choose model:</span>
              </div>
              <div style={{ display: 'flex', alignItems: 'center' }}>
                <RadioButton inputId="model1" name="model" value="googlenet" onChange={(e) => setModel(e.value)} checked={model === 'googlenet'} />
                <label htmlFor="model1" style={{ marginLeft: '5px' }}>GoogleNet</label>
              </div>
              <div style={{ display: 'flex', alignItems: 'center' }}>
                <RadioButton inputId="model2" name="model" value="vgg16" onChange={(e) => setModel(e.value)} checked={model === 'vgg16'} />
                <label htmlFor="model2" style={{ marginLeft: '5px' }}>VGG16</label>
              </div>
              <div style={{ display: 'flex', alignItems: 'center' }}>
                <RadioButton inputId="model3" name="model" value="resnet" onChange={(e) => setModel(e.value)} checked={model === 'resnet'} />
                <label htmlFor="model3" style={{ marginLeft: '5px' }}>ResNet</label>
              </div>
              <div style={{ display: 'flex', alignItems: 'center' }}>
                <RadioButton inputId="model3" name="model" value="custom" onChange={(e) => setModel(e.value)} checked={model === 'custom'} />
                <label htmlFor="model3" style={{ marginLeft: '5px' }}>Custom</label>
              </div>
            </div>
          </Card>
        </div>


        <div className="p-col-12 p-md-6 p-lg-6">
          <Card title="" className="card">
            <div className="content">
              <ClassificationComponent model={model} toast={toast} />
            </div>
          </Card>
        </div>
      </div>
    </div>
  );
}

export default App;
