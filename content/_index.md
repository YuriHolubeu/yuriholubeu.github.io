---
# Leave the homepage title empty to use the site title
title: ""
date: 2022-10-24
type: landing

design:
  # Default section spacing
  spacing: "3rem"

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
      text: ""
      # Show a call-to-action button under your biography? (optional)
      button:
        text: Download CV
        url: uploads/resume.pdf
    design:
      css_class: dark
      background:
        color: black
        image:
          # Add your image background to `assets/media/`.
          filename: stacked-peaks.svg
          filters:
            brightness: 1.0
          size: cover
          position: center
          parallax: false




#
#
#   !!!!!!  nbviewer.org обновляет большие файлы по одному дню (альтернатива -  вписывать в код коммит, что неудобно, ибо потом придется менять их)
#
#
#

  
  
  - block: markdown
    id: Research
    content:
      title: <h1>Research </h1>
      subtitle: ''

      text: |-    
          <p style="line-height: 1.2; font-size: 1rem;">
            In this section, there are my main papers.
          </p>

          <ul class="link-list">
            <li>
              Master's thesis:
              <a href="/notes/masters_thesis_GF-MTJJ.pdf" target="_blank" rel="noopener noreferrer">
                Green's Function for Multiterminal Josephson Junctions
              </a>
            </li>
          </ul>

          <ul style="line-height: 1.2; margin: 0; padding-left: 1.2em;">
            <li style="margin-bottom: 0.2em;">
              Master's thesis:
              <a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/some%20projects/masters_thesis_GF-MTJJ.pdf"
                target="_blank"
                style="overflow-wrap: anywhere; word-break: break-word;">
                Green's Function for Multiterminal Josephson Junctions
              </a>
            </li>

            <li style="margin-bottom: 0.2em;">
              Bachelor's thesis:
              <a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/some%20projects/bach_thesis_lensing.pdf"
                target="_blank"
                style="overflow-wrap: anywhere; word-break: break-word;">
                Gravitational Lensing of Binary Systems
              </a>
            </li>
          </ul>





    design:
      columns: '1'

  
  - block: markdown
    id: notes
    content:
      title: <h1>Notes on Basic Physics </h1>
      subtitle: ''

      text: |-    

        <p style="line-height: 1.2;""><font size="3"> 
        For many years I have been studying physics and mathematics using the a philosophy of doing science which I describe <a  href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/learning physics.pdf" target="_blank">here</a>. In a nutshell, I believe that by structuring information in digital notes and separating the key methods and properties into a dedicated section, one can achieve a deeper understanding. The notes below are an unfinished demo version, which demonstrates how they will look after several years of development. Nevertheless, they contain many methods and many problems for practice with solutions. 
        </font></p>

        <p style="line-height: 1.2;""><font size="3"> 
        In this section, there are notes on the most important parts of physics. 
        
        </font></p>


        <ul style="line-height: 1.2; margin: 0; padding-left: 1.2em;">
          <li style="margin-bottom: 0.2em;">
            <a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/basic%20physics/%E2%96%A0%20%20mechanics.pdf"
              target="_blank" rel="noopener noreferrer"
              style="overflow-wrap: anywhere; word-break: break-word;">
              mechanics
            </a>
          </li>
          <li style="margin-bottom: 0.2em;">
            <a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/basic%20physics/◊%20%20field%20theory.pdf"
              target="_blank" rel="noopener noreferrer"
              style="overflow-wrap: anywhere; word-break: break-word;">
              field theory
            </a>
          </li>
          <li style="margin-bottom: 0.2em;">
            <a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/basic%20physics/◊%20gravity.pdf"
              target="_blank" rel="noopener noreferrer"
              style="overflow-wrap: anywhere; word-break: break-word;">
              gravity
            </a>
          </li>
          <li style="margin-bottom: 0.2em;">
            <a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/basic%20physics/●%20%20quantum%20mechanics.pdf"
              target="_blank" rel="noopener noreferrer"
              style="overflow-wrap: anywhere; word-break: break-word;">
              quantum mechanics
            </a>
          </li>
          <li style="margin-bottom: 0.2em;">
            <a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/basic%20physics/◘%20quantum%20field%20theory.pdf"
              target="_blank" rel="noopener noreferrer"
              style="overflow-wrap: anywhere; word-break: break-word;">
              quantum field theory
            </a>
          </li>
          <li style="margin-bottom: 0.2em;">
            <a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/basic%20physics/☐%20%20statistical%20physics.pdf"
              target="_blank" rel="noopener noreferrer"
              style="overflow-wrap: anywhere; word-break: break-word;">
              statistical physics
            </a>
          </li>
          <li style="margin-bottom: 0.2em;">
            <a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/basic%20physics/☐%20condensed%20matter.pdf"
              target="_blank" rel="noopener noreferrer"
              style="overflow-wrap: anywhere; word-break: break-word;">
              condensed matter
            </a>
          </li>
          <li style="margin-bottom: 0.2em;">
            <a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/basic%20physics/♣%20%20electrodynamics.pdf"
              target="_blank" rel="noopener noreferrer"
              style="overflow-wrap: anywhere; word-break: break-word;">
              electrodynamics
            </a>
          </li>
          <li style="margin-bottom: 0.2em;">
            <a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/basic%20physics/☼%20kinetics.pdf"
              target="_blank" rel="noopener noreferrer"
              style="overflow-wrap: anywhere; word-break: break-word;">
              kinetics
            </a>
          </li>
          <li style="margin-bottom: 0.2em;">
            <a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/basic%20physics/❀%20continuum%20mechanics.pdf"
              target="_blank" rel="noopener noreferrer"
              style="overflow-wrap: anywhere; word-break: break-word;">
              continuum mechanics
            </a>
          </li>
        </ul>
        
        </div>













    design:
      columns: '1'
          
  - block: markdown
    id: othernotes
    content:
      title: <h1>Extra Notes</h1>
      subtitle: ''

      text: |-    


        

        <p style="line-height: 1.2;""><font size="3">   
        From time to time I study mathematics or some specific fields of physics, and below are my notes on some of the most important of them.
          </font></p>



        <table border="0">
        <tr>
        <td><b style="font-size:20px">Notes on Basic Mathematics </b></td>
        <td><b style="font-size:20px">Notes on Specific Physics</b></td>
        </tr>
        <tr>
        <td>
        
          <ul class="link-list">
          
          <li><a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/mathematics/■%20%20mathematical analysis.pdf" target="_blank" rel="noopener noreferrer">mathematical analysis</a></li>
          
          <li><a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/mathematics/■%20complex analysis.pdf" target="_blank" rel="noopener noreferrer">complex analysis</a></li>
          
          <li><a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/mathematics/◊  differential equations.pdf" target="_blank" rel="noopener noreferrer">differential equations</a></li>
          
          <li><a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/mathematics/◊  partial differential equations.pdf" target="_blank" rel="noopener noreferrer">partial diff. equations</a></li>
          
          <li><a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/mathematics/◊ oscillations.pdf" target="_blank" rel="noopener noreferrer">oscillations</a></li>
          
          <li><a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/mathematics/■ special functions.pdf" target="_blank" rel="noopener noreferrer">special functions</a></li>
          
          <li><a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/mathematics/☐  algebra.pdf" target="_blank" rel="noopener noreferrer">algebra</a></li>
          
          <li><a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/mathematics/☐ linear algebra.pdf" target="_blank" rel="noopener noreferrer">linear algebra</a></li>
          
          <li><a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/mathematics/♣%20%20probability%20theory.pdf" target="_blank" rel="noopener noreferrer">probability theory</a></li>
          
          <li><a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/mathematics/◘ differential geometry.pdf" target="_blank" rel="noopener noreferrer">differential geometry</a></li>
       
        </ul>


        </div>





        </td>
        <td>


        <ul class="link-list">
          
          <li><a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/specific%20physics/❁%20special%20field%20and%20gravity%20theories.pdf" target="_blank" rel="noopener noreferrer">special field theories</a></li>
          
          <li><a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/specific%20physics/◊%20cosmology.pdf" target="_blank" rel="noopener noreferrer">cosmology</a></li>
          
          <li><a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/specific%20physics/☐%20thermodynamics.pdf" target="_blank" rel="noopener noreferrer">thermodynamics</a></li>
          
          <li><a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/specific%20physics/♣%20magnetism.pdf" target="_blank" rel="noopener noreferrer">magnetism</a></li>
          
          <li><a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/specific%20physics/♣%20optics.pdf" target="_blank" rel="noopener noreferrer">optics</a></li>
          
          <li><a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/specific%20physics/☐%20superconductivity.pdf" target="_blank" rel="noopener noreferrer">superconductivity</a></li>

          <li><a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/specific%20physics/●%20quantum%20information%20theory.pdf" target="_blank" rel="noopener noreferrer">quantum information</a></li>
        </ul>


        </div>


        
        </td>
        </tr>
        </table>
        
        












          
  - block: markdown
    id: researchnotes
    content:
      title: <h1>Notes on Some Research Projects in Physics</h1>
      subtitle: ''
      text: |-
    
        <p style="line-height: 1.2;""><font size="3"> 
        I had several research projects, which didn't lead to the creation of articles, but I tried my best and made notes on each. One of the projects below is currently my main project.
        </font></p>

          <ul class="link-list">
            <li>
              <a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/some%20projects/☐ spin models with dissipation p1.pdf" target="_blank" rel="noopener noreferrer">
                spin models with dissipation part 1
              </a>, 
              <a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/some%20projects/☐ spin models with dissipation p2.pdf" target="_blank" rel="noopener noreferrer">
                part 2
              </a>
            </li>
            <li>
              <a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/some%20projects/☐ Green's function special methods.pdf" target="_blank" rel="noopener noreferrer">
                Green's function special methods for condensed matter
              </a>
            </li>
            <li>
              <a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/some%20projects/☐ sc junctions p1.pdf" target="_blank" rel="noopener noreferrer">
                superconductive junctions part 1
              </a>, 
              <a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/some%20projects/☐ sc junctions p2.pdf" target="_blank" rel="noopener noreferrer">
                part 2
              </a>
            </li>
            <li>
              <a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/some%20projects/◘%20waveguide%20QED.pdf" target="_blank" rel="noopener noreferrer">
                waveguide QED
              </a>
            </li>
            <li>
              <a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/some%20projects/◊%20gravitational%20lensing.pdf" target="_blank" rel="noopener noreferrer">
                gravitational lensing
              </a>
            </li>
            <li>
              <a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/some%20projects/◊%20gravitational%20waves.pdf" target="_blank" rel="noopener noreferrer">
                gravitational waves
              </a>
            </li>
            <li>
              <a href="https://nbviewer.org/github/YuriHolubeu/Notes/blob/main/some%20projects/❁%20duality%20in%20special%20field%20theories.pdf" target="_blank" rel="noopener noreferrer">
                duality in special field theories
              </a>
            </li>
          </ul>


        </div>



  - block: markdown
    id: diplomas
    content:
      title: <h1>Diplomas</h1>
      subtitle: ''
      text: |-

        <div style="display: flex; justify-content: center; gap: 1em; flex-wrap: wrap;">
          <div style="flex: 1 1 300px; text-align: center; max-width: 500px;">
            <img src="/media/bd.jpg" alt="Bachelor's Diploma from MIPT" style="width: 100%; height: auto;">
            <div>Bachelor's Diploma from MIPT</div>
          </div>
          <div style="flex: 1 1 314px; text-align: center; max-width: 500px;">
            <img src="/media/md.jpg" alt="Master's Diploma from KU Leuven" style="width: 100%; height: auto;">
            <div>Master's Diploma from KU Leuven<br>(with distinction)</div>
          </div>
        </div>











        



---


