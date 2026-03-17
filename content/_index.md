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





  - block: markdown
    id: researchnotes_old
    content:
      title: <h1>Notes on Current Research Projects</h1>
      subtitle: ''
      text: |-


        <ul class="link-list">


          <li>
            <a href="/some%20projects/_polarons%20p1.pdf" target="_blank">polarons part 1</a>,
            <a href="/some%20projects/_polarons%20p2.pdf" target="_blank">part 2</a>
          </li>

          <div style="height: 0.5em;"></div>


          <li style="margin-bottom: 0.2em;">
            <a href="/some%20projects/_charge%20density%20waves.pdf" target="_blank">charge density waves</a>
          </li>

          <div style="height: 0.5em;"></div>


          <li>
            <a href="/some%20projects/_nonequilibrium%20SC%20p1.pdf" target="_blank">nonequilibrium superconductivity part 1</a>,
            <a href="/some%20projects/_nonequilibrium%20SC%20p2.pdf" target="_blank">part 2</a>
          </li>


        </ul>





  - block: markdown
    id: researchnotes_current
    content:
      title: <h1>Notes on Research Projects That I Am Not Doing Now</h1>
      subtitle: ''
      text: |-

        <p style="line-height: 1.2;"><font size="3"></font></p>
        
        
        <ul style="line-height: 1.2; margin: 0 0 1em 0; padding-left: 1.2em;">
          <li style="margin-bottom: 0.2em;">
            Master's thesis:
            <a href="/some%20projects/masters_thesis_GF-MTJJ.pdf" target="_blank">
              Green's Function for Multiterminal Josephson Junctions
            </a>
          </li>

          <li style="margin-bottom: 0.2em;">
            Bachelor's thesis:
            <a href="/some%20projects/bach_thesis_lensing.pdf" target="_blank">
              Gravitational Lensing of Binary Systems
            </a>
          </li>
        </ul>

        
        <ul class="link-list">
          

          <li class="extra-space">
            <a href="/some%20projects/_spin models%20with%20dissipation%20p1.pdf" target="_blank" rel="noopener noreferrer">
              spin models with dissipation part 1
            </a>,
            <a href="/some%20projects/_spin%20models%20with dissipation%20p2.pdf" target="_blank" rel="noopener noreferrer">
              part 2
            </a>
          </li>

          <li class="extra-space">
            <a href="/some%20projects/☐%20Green's%20function%20special%20methods.pdf" target="_blank" rel="noopener noreferrer">
              Green's function special methods for condensed matter
            </a>
          </li>

          <li>
            <a href="/some%20projects/☐%20sc%20junctions%20p1.pdf" target="_blank" rel="noopener noreferrer">
              superconductive junctions part 1
            </a>,
            <a href="/some%20projects/☐%20sc%20junctions%20p2.pdf" target="_blank" rel="noopener noreferrer">
              part 2
            </a>
          </li>

          <li class="extra-space">
            <a href="/some%20projects/_waveguide%20QED.pdf" target="_blank" rel="noopener noreferrer">
              waveguide QED
            </a>
          </li>

          <li class="extra-space">
            <a href="/some%20projects/◊%20wave%20optics%20for%20GL%20p1.pdf" target="_blank" rel="noopener noreferrer">
              wave optics in gravitational lensing part 1
            </a>,
            <a href="/some%20projects/◊%20wave%20optics%20for%20GL%20p2.pdf" target="_blank" rel="noopener noreferrer">
              part 2
            </a>
          </li>

          <li>
            <a href="/some%20projects/◊%20gravitational%20waves.pdf" target="_blank" rel="noopener noreferrer">
              gravitational waves
            </a>
          </li>

          <li class="extra-space">
            <a href="/some%20projects/❁%20duality%20in%20special%20field%20theories.pdf" target="_blank" rel="noopener noreferrer">
              duality in special field theories
            </a>
          </li>
        </ul>










  - block: markdown
    id: notes
    content:
      title: <h1>Notes on Basic Physics</h1>
      subtitle: ''
      text: |-

        <p style="line-height: 1.2;">
          <font size="3">
          Guided by a general philosophy of doing science (outlined <a href="/learning%20physics.pdf" target="_blank">here</a>), I have developed a set of physics notes. These can be seen as an attempt to rewrite Landau's books in a form that is more relevant today. However, it does not make sense to focus on further developing them at the moment, as this work does not generate income. It is more productive to concentrate on one or two research directions rather than spread efforts across many general topics in physics. Currently, I update the notes only as needed.
          </font>
        </p>

        <ul style="line-height: 1.2; margin: 0; padding-left: 1.2em;">
          <li><a href="/basic%20physics/_mechanics.pdf" target="_blank">mechanics</a></li>
          <li><a href="/basic%20physics/_field%20theory.pdf" target="_blank">field theory</a></li>
          <li><a href="/basic%20physics/_gravity.pdf" target="_blank">gravity</a></li>
          <li><a href="/basic%20physics/_quantum%20mechanics.pdf" target="_blank">quantum mechanics</a></li>
          <li><a href="/basic%20physics/_quantum%20field%20theory.pdf" target="_blank">quantum field theory</a></li>
          <li><a href="/basic%20physics/_statistical%20physics.pdf" target="_blank">statistical physics</a></li>
          <li><a href="/basic%20physics/_condensed%20matter.pdf" target="_blank">condensed matter</a></li>
          <li><a href="/basic%20physics/_electrodynamics.pdf" target="_blank">electrodynamics</a></li>
          <li><a href="/basic%20physics/_kinetics.pdf" target="_blank">kinetics</a></li>
          <li><a href="/basic%20physics/_continuum%20mechanics.pdf" target="_blank">continuum mechanics</a></li>
        </ul>













    design:
      columns: '1'
          
  - block: markdown
    id: othernotes
    content:
      title: <h1>Extra Notes</h1>
      subtitle: ''

      text: |-    


        

        <p style="line-height: 1.2;""><font size="3">   
        Physics and mathematics cover many specialized topics, so I created notes on those areas that are most likely to be useful. Such notes will remain untouched, unless they are needed for my research.
        </font></p>



        <table border="0">
        <tr>
        <td><b style="font-size:20px">Notes on Basic Mathematics </b></td>
        <td><b style="font-size:20px">Notes on Specific Physics</b></td>
        </tr>
        <tr>
        <td>
        
          <ul class="link-list">
          
          <li><a href="/mathematics/_mathematical%20analysis.pdf" target="_blank" rel="noopener noreferrer">mathematical analysis</a></li>
          
          <li><a href="/mathematics/_complex%20analysis.pdf" target="_blank" rel="noopener noreferrer">complex analysis</a></li>
          
          <li><a href="/mathematics/_differential%20equations.pdf" target="_blank" rel="noopener noreferrer">differential equations</a></li>
          
          <li><a href="/mathematics/_partial differential equations.pdf" target="_blank" rel="noopener noreferrer">partial diff. equations</a></li>
          
          <li><a href="/mathematics/_oscillations.pdf" target="_blank" rel="noopener noreferrer">oscillations</a></li>
          
          <li><a href="/mathematics/_algebra.pdf" target="_blank" rel="noopener noreferrer">algebra</a></li>
          
          <li><a href="/mathematics/_linear%20algebra.pdf" target="_blank" rel="noopener noreferrer">linear algebra</a></li>
          
          <li><a href="/mathematics/_probability%20theory.pdf" target="_blank" rel="noopener noreferrer">probability theory</a></li>
          
          <li><a href="/mathematics/_differential%20geometry.pdf" target="_blank" rel="noopener noreferrer">differential geometry</a></li>
       
        </ul>


        </div>





        </td>
        <td>


        <ul class="link-list">
          
          <li><a href="/specific%20physics/_sp field and gravity theories.pdf" target="_blank" rel="noopener noreferrer">special field theories</a></li>
          
          <li><a href="/specific%20physics/_cosmology.pdf" target="_blank" rel="noopener noreferrer">cosmology</a></li>
          
          <li><a href="/specific%20physics/_thermodynamics.pdf" target="_blank" rel="noopener noreferrer">thermodynamics</a></li>
          
          <li><a href="/specific%20physics/_magnetism.pdf" target="_blank" rel="noopener noreferrer">magnetism</a></li>
          
          <li><a href="/specific%20physics/_optics.pdf" target="_blank" rel="noopener noreferrer">optics</a></li>
          
          <li><a href="/specific%20physics/_superconductivity.pdf" target="_blank" rel="noopener noreferrer">superconductivity</a></li>

          <li><a href="/specific%20physics/_quantum%20information.pdf" target="_blank" rel="noopener noreferrer">quantum information</a></li>
          
          <li><a href="/specific%20physics/_particle%20physics.pdf" target="_blank" rel="noopener noreferrer">particle physics</a></li>
          
        </ul>


        </div>


        
        </td>
        </tr>
        </table>
        
        













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




  - block: markdown
    id: updates
    subtitle: "updates"
    weight: 20
    content:
      title:  <h1>🧾 Selected Updates</h1>
      text: |


        - **17.03.2026** — I am abandoning the idea of writing physics books. I used this approach for about 6 years, I learned a lot, but this project is still far to be finished. Without grants to support it, I realized it is easier to focus on producing high-quality research than to write such books. I will focus a lot on them again someday in the future. Maybe. Anyway, such activity gives a lot of understanding, so I am motivated to return to it someday.
        

        - **28.02.2026** — The note on condensed matter became the first one that exceeded 3000 pages.
        

        - **30.11.2025** — The translation of tables of contents of all the notes here to English is finished.
        

        - **03.11.2025** — The translation of tables of contents of the main notes on physics to English is finished.


        - **October 2025** — I realized I could make this page more lively by occasionally highlighting the main changes in my notes and my research.







        



---


